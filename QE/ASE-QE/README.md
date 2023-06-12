
# Quantum Espresso + ASE: Building and Running Your First QE Input (6 minutes)

## Prerequisites for the Course:

To follow along with this course, please ensure you have the following:

- **ASE** (Atomic Simulation Environment) installed.
- **Quantum Espresso** installed.
- Basic knowledge of Python data types (such as lists and dictionaries).
- Calculator setup: Find the path of the installed `pw.x` executable by using the command `which pw.x` and add the following line to the end of your `~/.bashrc` file:

```bash
export ASE_ESPRESSO_COMMAND="/path/to/pw.x -in PREFIX.pwi > PREFIX.pwo"
```

Step 0: Download the CIF file and required pseudo-potentials and copy them to your working directory.

There are two different methods to submit your job:

**Method 1:**

- Build your input and submit your job inside the ASE environment.

  - Step 1: Open an IPython environment and import ASE libraries.

    ```shell
    :~ $ ipython
    ```

    ```python
    from ase.io import read, write
    from ase.calculators.espresso import Espresso
    ```

  - Step 2: Build an ASE Atoms object by reading the CIF file.

    ```python
    my_ase_obj = read("GaAs.cif")
    ```

  - Step 3: Define your input settings as a Python dictionary.

    ```python
    input_data = {'prefix': "myprefix", 'electron_maxstep': 200, 'outdir': "./", 'pseudo_dir': "./",
                  'tstress': True, 'tprnfor': True, 'calculation': 'scf', 'ecutrho': 240, 'verbosity': 'high',
                  'ecutwfc': 30, 'diagonalization': 'david', 'occupations': 'smearing', 'smearing': 'mp',
                  'mixing_mode': 'plain', 'mixing_beta': 0.7, 'degauss': 0.001, 'nspin': 1}
    ```

**Note:** You can modify the above input as desired...

  - Step 4: Define a dictionary in Python containing your pseudo files. In our example:

    ```python
    pseudodict = {"Ga": "Ga.pbe-dnl-rrkjus_psl.1.0.0.UPF", "As": "As.pbe-n-rrkjus_psl.1.0.0.UPF"}
    ```

  - Step 5: Add the Espresso calculator to the ASE Atoms object as follows:

    ```python
    my_ase_obj.calc = Espresso(pseudopotentials=pseudodict, input_data=input_data, kpts=(2, 2, 2))
    ```

  - Step 6: Submit the Quantum Espresso job.

    ```python
    my_ase_obj.get_potential_energy()
    ```

  - Step 7: Get the output data.

    ```python
    output = read("espresso.pwo")
    output.get_potential_energy()
    output.get_forces()
    output.get_stress()
    ```

**Method 2 (Alternative):**

Repeat steps 1 to 4 from Method 1...

  - Step 5: After defining `my_ase_obj`, `pseudodict`, and `input_data`, we can build a Quantum Espresso input file using the `write` function:

    ```python
    write("new.pwi", my_ase_obj, pseudopotentials=pseudodict, input_data=input_data, kpts=(2, 

2, 2))
    ```

  - Step 6: Execute the `pw` command in the Linux terminal.

    ```bash
    ~ $ pw.x < new.pwi > new.pwo
    ```
