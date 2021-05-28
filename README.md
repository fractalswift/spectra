# spectra

# v1

### To download

1. Open command prompt

2. Run `git clone https://github.com/fractalswift/spectra.git`

3. Navigate to spectra: `cd spectra`

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

1. Activate your virtual env if it is not activated: `activate`. If you don't have a virtual env don't worry about this.

2. Drop your json files into the data_input folder

3. Run `python process_data.py`

4. Graphs hopefully now appear in graph_output

### Trouble shooting

The virtual env stuff just creates an isolated environment for python dependencies. If it doesn't work you can skip it but will just have to make sure you have the right dependencies (in this case just pandas). It might also require that you run the file with "python3" instead of just "python":

      python3 process_data.py
