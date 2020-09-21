# IPMan

<h2>Tiny tool to find reverse IP information in bulk</h2>

Takes in a list of IP addresses in a text file format and outputsa json with information about that specific IP including location, hostname, city, region and service provider. Utilizes python's ipinfo package.


<h2>Installation:</h2>

1. Initialise a virtual environment using your favourite tool (I prefer venv)<br>
       a) Install virtualenv: 
              <b>pip install virtualenv</b><br>
       b) Creating new virtualenv: 
             <b> virtualenv virtual_environment_name </b><br>
       c) Activating virtualenv:
              <b>./virtual_environment_name/Scripts/activate</b><br>

2. Install requirements by using:
       <b>pip install -r requirements.txt</b>
       
<h2>Run:</h2>

1. To run with existing sample input IP file:
  <b>python IPMan.py input.txt</b>

2. To run with a new input file:
  <b>python IPMan.py input_filename.txt</b>

3. To specify both an input file and an output file:
  <b>python IPMan.py input_filename.txt output_filename.json</b> 
  
