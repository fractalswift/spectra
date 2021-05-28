# spectra

# v1

### To set up:

1.  create virtual env. This isn't essential but will likely save you a headache later:

        python3 -m venv venv

2.  Activate virtual env

    - Mac/linux:

      `source venv/bin/activate`

    - Windows:

      `activate`

    - (If this doesn't work check https://programwithus.com/learn/python/pip-virtualenv-windows or just skip to step 3)

3.  Install dependencies:

    `pip install -r requirements.txt`

### To use:

1. Drop your json files into the data_input folder

2. Run `python process_data.py`

3. Graphs hopefully now appear in graph_output
