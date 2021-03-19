import copy
from typing import Any, Collection, Dict, List, Set, Union

from tabml.utils.pb_helpers import parse_feature_config_pb


class _Feature:
    def __init__(self, index: int, dtype: str, dependencies: Union[List, None] = None):
        self.index = index
        self.dependents: List[str] = []
        self.dtype = dtype
        if dependencies is None:
            self.dependencies = []
        else:
            self.dependencies = dependencies


class FeatureConfigHelper:
    """A config helper class for feature manager.

    Attributes:
        _config:
            A protobuf object parsed from a pb text file.
        raw_data_dir:
            A string of directory to raw data.
        dataset_name:
            A string of the dataset name
        base_features:
            A list of base feature names in the config.
        transforming_features:
            A list of transforming feature names in the config.
        all_features:
            A list of all features in the config.
        feature_metadata:
            A dict of {feature_name: (index, dtype, list of its dependents)}.
            This is useful when finding all dependents of one feature.
    """

    def __init__(self, pb_config_path: str):
        self._config = parse_feature_config_pb(pb_config_path)
        self.raw_data_dir = self._config.raw_data_dir
        self.dataset_name = self._config.dataset_name
        self.base_features = [feature.name for feature in self._config.base_features]
        self.transforming_features = [
            transforming_feature.name
            for transforming_feature in self._config.transforming_features
        ]
        self.all_features = self.base_features + self.transforming_features
        self._validate()
        self.feature_metadata: Dict[str, _Feature] = {}
        self._build_feature_metadata()

    def _validate(self):
        self._validate_indexes()
        self._validate_uniqueness()
        self._validate_dependency()

    def _validate_indexes(self):
        """Checks if indexes are positive and monotonically increasing."""
        indexes = [
            transforming_feature.index
            for transforming_feature in self._config.transforming_features
        ]
        if not (
            indexes[0] > 0
            and all(
                [
                    index_i < index_ip1
                    for (index_i, index_ip1) in zip(indexes[:-1], indexes[1:])
                ]
            )
        ):
            raise ValueError(
                "Feature indexes must be a list of increasing positive integers. "
                f"Got indexes = {indexes}"
            )

    def _validate_uniqueness(self):
        _check_uniqueness(self.all_features)

    def _validate_dependency(self):
        """Checks if all dependencies of a transforming feature exists."""
        # initialize from base_features then gradually adding transforming_feature
        features_so_far = self.base_features.copy()
        for feature in self._config.transforming_features:
            for dependency in feature.dependencies:
                assert (
                    dependency in features_so_far
                ), "Feature {} depends on feature {} that is undefined.".format(
                    feature.name, dependency
                )
            features_so_far.append(feature.name)

    def _build_feature_metadata(self):
        for feature in self._config.base_features:
            # all base features are considered to have index 0
            self.feature_metadata[feature.name] = _Feature(index=0, dtype=feature.dtype)

        for feature in self._config.transforming_features:
            self.feature_metadata[feature.name] = _Feature(
                index=feature.index,
                dtype=feature.dtype,
                dependencies=feature.dependencies,
            )
            for dependency in feature.dependencies:
                self.feature_metadata[dependency].dependents.append(feature.name)

    def sort_features(self, feature_names: List[str]) -> List[str]:
        return sorted(feature_names, key=lambda x: self.feature_metadata[x].index)

    def find_dependencies(self, feature_name: str) -> List[str]:
        return self.feature_metadata[feature_name].dependencies

    def get_dependencies_recursively(self, features: List[str]) -> List[str]:
        """Gets all dependencies of a list of features recursively.

        The input list should also be in the result.
        """
        queue = copy.copy(features)
        seen: List[str] = []
        while queue:
            feature = queue.pop(0)
            if feature in seen:
                continue
            seen.append(feature)
            queue.extend(self.find_dependencies(feature))
        return self.sort_features(seen)

    def find_dependents(self, feature_name: str) -> List[str]:
        """Finds all features that are directly/indirectly dependent on a feature.

        This is necessary when we want to update one feature. All of its dependents also
        need to be updated. The list of returning features is required to be in the
        order determined by their indexes in the proto config.

        Notes:
            * If "b" is a dependency of "a" then "a" is a dependent of "b".
            * If "a" is a dependent of "b" and "b" is a dependent of "c" then "a" is a
              dependent of "c".
        """
        # BFS to find all dependents
        dependents: List[str] = []
        queue = self.feature_metadata[feature_name].dependents
        while queue:
            feature = queue.pop(0)
            if feature in dependents:
                continue
            dependents.append(feature)
            queue.extend(self.feature_metadata[feature].dependents)
        return self.sort_features(dependents)

    def append_dependents(self, feature_names: List[str]) -> List[str]:
        """Finds all dependents of a list of features then appends them to the list.

        This will be used when multiple features need to be updated or remove. For the
        first case, all dependents also need to be updated. For the second case, it's
        required that there is no dependent in the remaining features.

        NOTE: the results should also contain the input feature_names.
        """
        all_features = feature_names
        for feature_name in feature_names:
            all_features.extend(self.find_dependents(feature_name))

        return self.sort_features(list(set(all_features)))

    def extract_config(self, transforming_features: List[str]):
        """Creates a minimum valid config that contains all transforming_features.

        Returns a protobuf with only a subset of transforming features and all of their
        dependencies.

        Args:
            transforming_features: a list of selected transforming features.

        Raises:
            ValueError if transforming_features contains an unknown features (not in the
            original config).
        """
        invalid_features = [
            feature
            for feature in transforming_features
            if feature not in self.transforming_features
        ]
        if invalid_features:
            raise ValueError(
                f"Features {invalid_features} are not in the original config."
            )
        all_relevant_features = self.get_dependencies_recursively(
            features=transforming_features
        )
        new_pb = copy.deepcopy(self._config)
        # we can't deriectly assign a list to a protobuf repeated field
        # https://tinyurl.com/y4m86cc4
        del new_pb.transforming_features[:]
        new_pb.transforming_features.extend(
            [
                transforming_feature
                for transforming_feature in self._config.transforming_features
                if transforming_feature.name in all_relevant_features
            ]
        )

        return new_pb


def _check_uniqueness(items: Collection) -> None:
    """Checks if an array containing unique elements.

    Args:
        items: A list of objects.

    Returns:
        Does not return anything. If this function passes, it means that all objects
        are unique.

    Raises:
        Assertion error with list of duplicate objects.
    """
    seen_items: Set[Any] = set()
    duplicates = set()
    for item in items:
        if item in seen_items:
            duplicates.add(item)
        seen_items.add(item)
    assert not duplicates, f"There are duplicate objects in the list: {duplicates}."