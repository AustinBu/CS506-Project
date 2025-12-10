import pytest
import pandas as pd
import pickle
import numpy as np
import os 

MODEL_FILE_PATH = 'model.pkl' 
EXPECTED_NUM_FEATURES = 42 

@pytest.fixture(scope="session")
def load_model():
    """Fixture to safely load the trained model."""
    if not os.path.exists(MODEL_FILE_PATH):
        pytest.skip(f"Model file not found at: {MODEL_FILE_PATH}")
    
    with open(MODEL_FILE_PATH, 'rb') as file:
        model = pickle.load(file)
    return model


@pytest.fixture
def create_test_sample():
    """Fixture to create the structured test sample DataFrame."""
    
    EXPECTED_COLUMNS = [
        'Price', 'Windows', 'Mac', 'Linux', 'Single-player', 'Multi-player', 'rating', 
        'day', 'month', 'year', 'primary_genre_Action (1)', 'primary_genre_Adventure (25)', 
        'primary_genre_Casual (4)', 'primary_genre_Design & Illustration (53)', 
        'primary_genre_Early Access (70)', 'primary_genre_Education (54)', 
        'primary_genre_Free to Play (37)', 'primary_genre_Game Development (60)', 
        'primary_genre_Gore (74)', 'primary_genre_Indie (23)', 
        'primary_genre_Massively Multiplayer (29)', 'primary_genre_Nudity (72)', 
        'primary_genre_RPG (3)', 'primary_genre_Racing (9)', 
        'primary_genre_Sexual Content (71)', 'primary_genre_Simulation (28)', 
        'primary_genre_Sports (18)', 'primary_genre_Strategy (2)', 
        'primary_genre_Unknown Genre (0)', 'primary_genre_Unknown Genre (21)', 
        'primary_genre_Unknown Genre (33)', 'primary_genre_Unknown Genre (34)', 
        'primary_genre_Unknown Genre (6)', 'primary_genre_Utilities (57)', 
        'primary_genre_Video Production (58)', 'primary_genre_Violent (73)', 
        'primary_genre_Web Publishing (59)', 'primary_genre_nan', 
        'Mode Category_Both', 'Mode Category_Multi-player only', 'Mode Category_None', 
        'Mode Category_Single-player only'
    ]

    sample_data = {
        'Price': 19.99, 'Windows': 1, 'Mac': 0, 'Linux': 0, 'Single-player': 1, 
        'Multi-player': 0, 'rating': 8.5, 'day': 15, 'month': 1, 'year': 2024,
        'primary_genre_RPG (3)': 1, 'Mode Category_Single-player only': 1
    }

    test_sample_df = pd.DataFrame([sample_data]).reindex(columns=EXPECTED_COLUMNS, fill_value=0)
    return test_sample_df


def test_sample_shape_is_correct(create_test_sample):
    """Test 1: Check that the input sample has the exact number of features expected by the model."""
    sample = create_test_sample
    assert sample.shape == (1, EXPECTED_NUM_FEATURES), f"Expected shape (1, {EXPECTED_NUM_FEATURES}), got {sample.shape}"


def test_prediction_output_is_valid(load_model, create_test_sample):
    """Test 2: Check that the model predicts a single integer class ID (0, 1, 2, 3, or 4)."""
    model = load_model
    sample = create_test_sample
    
    prediction = model.predict(sample)
    
    assert prediction.shape == (1,), f"Expected prediction shape (1,), got {prediction.shape}"
    
    assert np.issubdtype(prediction.dtype, np.integer), "Prediction output should be an integer type."
    
    assert 0 <= prediction[0] <= 4, f"Prediction {prediction[0]} is outside the valid class range (0-4)."