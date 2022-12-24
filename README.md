# Permissive Image-Caption Dataset Preparation

Preprocessor using Unsplash Lite (25,000) dataset to create a dataset for training text-image models with 512x512 bitmaps. The dataset is available at [Unsplash](https://unsplash.com/data). No images are stored on this repository.

## License

Code is available under the [BSD 3-Clause License](LICENSE). Usage of the Unsplash dataset must be in accordance with the [Unsplash License](https://unsplash.com/license).

## Usage
1. Obtain the Unsplash Lite (25,000) dataset from [Unsplash](https://unsplash.com/data). See [unsplash/datasets on Github](https://github.com/unsplash/datasets) for more information.
2. Clone this repository.
3. Run `scraper.py` to download the images from the dataset and resize them.