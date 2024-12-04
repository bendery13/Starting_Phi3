import pytest
from Project3 import openFile, Ratings

# 1. Test openFile function with a valid file
def test_open_file_valid(tmp_path):
    file_content = (
        "Review 1 text here.\n"
        "-------------------------\n"
        "Review 2 text here.\n"
        "-------------------------\n"
    )
    test_file = tmp_path / "valid_reviews.txt"
    test_file.write_text(file_content)
    
    reviews = openFile(str(test_file))
    assert len(reviews) == 2
    assert reviews[0].strip() == "Review 1 text here."
    assert reviews[1].strip() == "Review 2 text here."

# 2. Test openFile function with an empty file
def test_open_file_empty(tmp_path):
    test_file = tmp_path / "empty_reviews.txt"
    test_file.write_text("")  # Create an empty file
    
    reviews = openFile(str(test_file))
    assert len(reviews) == 0

# 3. Test Ratings class methods
def test_ratings_methods():
    ratings = Ratings()
    assert ratings.get_positives() == 0
    assert ratings.get_neutrals() == 0
    assert ratings.get_negatives() == 0

    ratings.add_positive()
    ratings.add_neutral()
    ratings.add_negative()

    assert ratings.get_positives() == 1
    assert ratings.get_neutrals() == 1
    assert ratings.get_negatives() == 1

def test_pull_ratings_mixed(tmp_path):
    file_content = (
        "Positive\n"
        "Neutral\n"
        "Negative\n"
        "Positive\n"
        "Negative\n"
    )
    test_file = tmp_path / "mixed_sentiments.txt"
    test_file.write_text(file_content)

    ratings = Ratings.pullRatings(str(test_file))
    assert ratings.get_positives() == 2
    assert ratings.get_neutrals() == 1
    assert ratings.get_negatives() == 2

# 4. Using pytest.mark.parametrize for parameterized testing
@pytest.mark.parametrize(
    "file_content, expected_positives, expected_neutrals, expected_negatives",
    [
        ("", 0, 0, 0),  # Empty file
        ("Positive\n", 1, 0, 0),  # Single positive review
        ("Neutral\nNeutral\n", 0, 2, 0),  # Two neutral reviews
        ("Negative\nNegative\nNegative\n", 0, 0, 3),  # Three negative reviews
    ],
)
# 5. Test that an empty file will not cause an error in the code
def test_pull_ratings_empty_file(tmp_path, file_content, expected_positives, expected_neutrals, expected_negatives):
    test_file = tmp_path / "test_file.txt"
    test_file.write_text(file_content)

    ratings = Ratings.pullRatings(str(test_file))
    assert ratings.get_positives() == expected_positives
    assert ratings.get_neutrals() == expected_neutrals
    assert ratings.get_negatives() == expected_negatives
