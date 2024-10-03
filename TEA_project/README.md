# EasyJSON

**EasyJSON** is a Python library that simplifies handling JSON data. It provides utilities for loading, saving, and manipulating JSON files with minimal code.

## Features
- Easy-to-use methods for loading and saving JSON.
- Automatic pretty-printing of JSON data.
- Methods for safely updating and querying JSON content.

## Installation

You can install the package via pip:

```bash
pip install easyjson
```

## Usage

```python
import easyjson as ej

# Load JSON data from a file
data = ej.load_json('data.json')

# Modify and save the data
data['new_key'] = 'new_value'
ej.save_json('data.json', data)
```

## Contributing

Feel free to open issues and submit pull requests! Check out our `CONTRIBUTING.md` for more details.

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.
