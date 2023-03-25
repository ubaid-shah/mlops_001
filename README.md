## MLOps project

This project is about Students data analysis and then thier marks prediction using Regression algorithm. After that every thing can be deployed using Machine Learning Pipeline.

The complete process includes the following steps:

### Step 1: Creating the folder structure and adding files into it

1. Create a project folder name mlops_001

2. Create a GitHub repo mlops_001

3. Start cmd and type ---- 

```cd Downloads/mlops_001```

4. in cmd type -----       ```code .```

it will start VSCode

5. Synch the GitHub repo with VSCode     

	a) Start a terminal in VSCode	
	
	b) Setup environment by --- ```conda create -p venv python==3.8 -y```
	
	c) Activate the environment by -- ```conda activate "C:\Users\user_name\folder\mlops_001\venv"```

6. set git configuration

	a) ```git config --global user.name "Username"```
	
	b) ```git config --global user.email "useremail"```

7. Now clone the GitHub repo
	
	a) initialize the reo --- ```git init```
	
	b) create a ```README.md``` file in the ```mlops_001``` folder
	
	c) ```git add README.md```
	
	d) ```git commit -m "first commit"```
	
	e) to check the status use -- ```git status```
	
	f) ```git branch -M main```
	
	g) ```git remote add origin https://github.com/profile/mlops_001.git```
	
	h) to check the files use --  ```git remote -v```
	
	i) to push all the files from staging area to ```git push -u origin main```
        
8. Create ```.gitignore``` file in github repo use default template

9. To get upto date info in VS code Use --  ```git pull```

10. create two files setup.py and requirements.txt

	a) ```setup.py``` is responsible for creating ML model as a package
	
	b) ```requirements.txt``` responsible for installing required packages for project 

11. create a folder named as ```src```. Inside this folder create a file ```__init__.py```

12. In src folder create a folder named as ```componenets```. Inside this folder create a file ```__init__.py```.Also create ```data_ingestion.py```, ```data_transformation.py``` and ```data_trainer.py```.

13. In src folder create a folder named as ```pipeline```. Inside this folder create a file ```__init__.py```. Also create ```train_pipline.py```, ```predict_pipeline.py```.

14. Create the files in the src folder as ```logger.py``` and ```exception.py```, ```utils.py```,

15. After writing code in the files add to the github repository


### Step2: EDA

1. Create a folder names as ```Notebook```. Inside that folder create a folder called ```Data```. In the data folder keep the ```csv file```. Inside the jupyter file create two files ```EDA_file.ipynb ```and ```training.ipynb```

2. create ipynb kernel in vs code to run jupyter notebook using -- 
 ```conda install -p "c:\Users\user_name\folder\mlops_001\venv" ipykernel --update-deps --force-reinstall```
 
3. write the code in EDA_file and training file and after that push to the repo 


### Step 3: Edit data_ingestion, data_transformation and data_trainer files

### Step 4: Create app.py for flask app
1. Create a folder named as ```templates``` in main repo and then create two files ```index.html``` and ```home.html```.

2. Give path of these files in ```app.py``` and run the file with ip - ```127.0.0.1:5000```

### Step5: Deploy the git hub repo in AWS for CI/CD operations
