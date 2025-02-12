# pipeline-functions

## Overview

`pipeline-functions` is a demonstration project showcasing various pipeline functions. This project aims to provide examples and best practices for implementing those functions in your workflows.

## Features

- Example pipeline functions
- Best practices for implementation
- Easy-to-follow code samples

## Project Structure

- [`.env_sample`](.env_sample ): Sample environment variables file.
- [`db_connection.py`](db_connection.py ): Contains functions for creating database connections.
- [`intelligent_retrieval.ipynb`](intelligent_retrieval.ipynb ): Jupyter notebook for intelligent data retrieval and analysis.
- [`LICENSE`](LICENSE ): License file for the project.
- [`meta_data_filtering.ipynb`](meta_data_filtering.ipynb ): Jupyter notebook for filtering metadata and interacting with the database.
- [`playground_for_chunking.ipynb`](playground_for_chunking.ipynb ): Jupyter notebook for experimenting with different data chunking methods.
- [`sample_data`](sample_data ): Directory containing sample data files.
  - `Bilge Ince.html`: Sample HTML file.
  - [`sample_data/books.csv`](sample_data/books.csv ): Sample CSV file containing book data from Goodreads.
  - `sample_k_means.pdf`: Sample PDF file from [my own blog post](https://medium.com/code-like-a-girl/finding-dominant-colour-on-an-image-b4e075f98097).

## Getting Started

### Installation

1. Clone the repository:

```bash
git clone https://github.com/bilge-ince/pipeline-functions-demo.git
cd pipeline-functions-demo
```

2. Install dependencies:

```sh
pip install -r requirements.txt
```

3. Set up the environment variables by copying `.env_sample` to `.env` and updating the values as needed.

### Usage

#### Metadata Filtering

The `meta_data_filtering.ipynb` notebook demonstrates how to filter metadata and interact with the database. 
It includes examples of reading data from a [Goodreads CSV file](https://www.kaggle.com/datasets/jealousleopard/goodreadsbooks) and inserting it into a database table. 

#### Intelligent Retrieval

The `intelligent_retrieval.ipynb` notebook provides examples of intelligent data retrieval and analysis, including visualizations using Plotly.

#### Data Chunking

The `chunking_methods.ipynb` notebook explores various methods for chunking data, including fixed-size chunking, recursive chunking, and semantic chunking.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

## License

This project is licensed under the Apache License 2.0. See the `LICENSE` file for more details.
