"""Tests for the 'ISO3' categorization."""
import pytest

import climate_categories


def test_categories():
    assert climate_categories.ISO3["DEU"].title == "Germany"
    assert len(climate_categories.ISO3) > 150


def test_eu():
    assert len(climate_categories.ISO3["EU-12"].children[0]) == 12
    assert len(climate_categories.ISO3["EU-15"].children[0]) == 15
    assert len(climate_categories.ISO3["EU-25"].children[0]) == 25
    assert len(climate_categories.ISO3["EU-27_2007"].children[0]) == 27
    assert len(climate_categories.ISO3["EU-28"].children[0]) == 28
    assert len(climate_categories.ISO3["EU-27_2020"].children[0]) == 27
    with pytest.raises(KeyError):
        climate_categories.ISO3["EU27"]

    assert climate_categories.ISO3["EU"] == climate_categories.ISO3["EU_2020"]


def test_unfccc():
    assert len(climate_categories.ISO3["Annex-I"].children[0]) == 43
    assert len(climate_categories.ISO3["Non-Annex-I"].children[0]) == 155
    # leaf children excludes EU, because EU is not a leaf
    assert len(climate_categories.ISO3["UNFCCC"].leaf_children[0]) == 197
    assert (
        climate_categories.ISO3["EU"] in climate_categories.ISO3["UNFCCC"].descendants
    )
