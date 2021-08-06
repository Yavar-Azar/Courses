

# QE+ASE 	(6 min)



## Build your first QE input and run it in 5 minutes



### Summary of Course Prerequisites:

- **ase** installed

- **quantum espresso** installed

- basic knowledge on python data types (list, dictionary, ...)

- Set up the calculator 

  Find the path of installed `pw.x ` using ``which pw.x` and add  this line to the end of your `~/.bashrc` 

  ```bash
  export ASE_ESPRESSO_COMMAND="/path/to/pw.x -in PREFIX.pwi > PREFIX.pwo"
  ```

  



Step-0 : Download your **cif** file and required **pseudo-potentials** and copy then in your work directory









There are two different way to submit your job

**First method:**

- build your input and submit your job inside ase environment

  - step 1

    open ipython env and import ase libraries

    ```shell
    :~ $ ipython
    ```

    ```python
    from ase.io import read, write
    from ase.calculators.espresso import Espresso
    ```

    

  - step 2

    build ase Atoms object by reading cif file

    ```python
    myaseobj=read("GaAs.cif")
    ```

    

  - step 3

    define your input setting as a python dictionary

    ```python
    inp_data={'prefix':"myprefix",'electron_maxstep':200,'outdir':"./",        'pseudo_dir':"./",'tstress':True,'tprnfor':True,'calculation':'scf', 
     'ecutrho':240,'verbosity':'high','ecutwfc':30, 'diagonalization': 'david', 'occupations':'smearing','smearing':'mp', 'mixing_mode':'plain', 'mixing_beta':0.7,'degauss':0.001, 'nspin':1}
    ```

------------

**Note**

you can modify above input as you wish ...

---------------------------------------------------
    

  - step 4

    define a dictionary in python containing your pseudo files, in our example

    ```python
    pseudodict={"Ga":"Ga.pbe-dnl-rrkjus_psl.1.0.0.UPF", "As":"As.pbe-n-rrkjus_psl.1.0.0.UPF"}
    ```

    

  - step 5

    add espresso calculator to ase Atoms object as follows:

    ```python
    myaseobj.calc=Espresso(pseudopotentials=pseudodict,input_data=inpdata, kpts=(2,2,2))
    ```

    

  - step 6

    submit quantum espresso job 

    ```python
    myaseobj.get_potential_energy()
    ```

    

  - step 7

    get output data

    ```python
    test=read("espresso.pwo")
    test.get_potential_energy()
    test.get_forces()
    test.get_stress()
    ```



- **Alternative method**

Repeat step1 to step4 ...

  - step 5

  after defining  **aseobj**, **psedudict** and **inputdata** we make can build a quantum espresso input file using `write`function:

  ```python
  write("new.pwi", myaseobj,pseudopotentials=pseudodict,input_data=inpdata, kpts=(2,2,2))
  ```

  - step 6

    and execute pw command in the linux terminal

    ```bash
    ~ $    pw.x < new.pwi > new.pwo
    ```

    

  

  
