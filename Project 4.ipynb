{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Titanic Data Analysis"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Background\n",
    "Titanic was a British passenger liner that sank in the North Atlantic Ocean in the early hours of 15 April 1912, after colliding with an iceberg during its maiden voyage from Southampton to New York City. There were an estimated 2,224 passengers and crew aboard, and more than 1,500 died, making it one of the deadliest commercial peacetime maritime disasters in modern history. (https://en.wikipedia.org/wiki/RMS_Titanic)\n",
    "## Question Definition\n",
    "According to some news, some groups of people were more likely to survive than others, such as women, children.  \n",
    "But it is doubtful whether the truth is like this or not.\n",
    "So the question is what factors affected the survived rate. "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Workflow\n",
    "To analyse the data, I follow these stages:  \n",
    "&emsp; 1.Coding the data  \n",
    "&emsp; 2.Checking the data  \n",
    "&emsp; 3.Structuring the data  \n",
    "&emsp; 4.Describing the data  \n",
    "&emsp; 5.Exploring the data  \n",
    "&emsp; 6.Visualising the data  \n",
    "&emsp; 7.Reporting the data"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Prepare Package"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "import seaborn as sns\n",
    "import matplotlib.pyplot as plt\n",
    "%matplotlib inline"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Acquire Data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "data=pd.read_csv('C:/Users/lenovo/project 4/titanic-data.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['PassengerId' 'Survived' 'Pclass' 'Name' 'Sex' 'Age' 'SibSp' 'Parch'\n",
      " 'Ticket' 'Fare' 'Cabin' 'Embarked']\n"
     ]
    }
   ],
   "source": [
    "print(data.columns.values)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style>\n",
       "    .dataframe thead tr:only-child th {\n",
       "        text-align: right;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: left;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>PassengerId</th>\n",
       "      <th>Survived</th>\n",
       "      <th>Pclass</th>\n",
       "      <th>Name</th>\n",
       "      <th>Sex</th>\n",
       "      <th>Age</th>\n",
       "      <th>SibSp</th>\n",
       "      <th>Parch</th>\n",
       "      <th>Ticket</th>\n",
       "      <th>Fare</th>\n",
       "      <th>Cabin</th>\n",
       "      <th>Embarked</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>Braund, Mr. Owen Harris</td>\n",
       "      <td>male</td>\n",
       "      <td>22.0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>A/5 21171</td>\n",
       "      <td>7.2500</td>\n",
       "      <td>NaN</td>\n",
       "      <td>S</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>Cumings, Mrs. John Bradley (Florence Briggs Th...</td>\n",
       "      <td>female</td>\n",
       "      <td>38.0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>PC 17599</td>\n",
       "      <td>71.2833</td>\n",
       "      <td>C85</td>\n",
       "      <td>C</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "      <td>Heikkinen, Miss. Laina</td>\n",
       "      <td>female</td>\n",
       "      <td>26.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>STON/O2. 3101282</td>\n",
       "      <td>7.9250</td>\n",
       "      <td>NaN</td>\n",
       "      <td>S</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>Futrelle, Mrs. Jacques Heath (Lily May Peel)</td>\n",
       "      <td>female</td>\n",
       "      <td>35.0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>113803</td>\n",
       "      <td>53.1000</td>\n",
       "      <td>C123</td>\n",
       "      <td>S</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>Allen, Mr. William Henry</td>\n",
       "      <td>male</td>\n",
       "      <td>35.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>373450</td>\n",
       "      <td>8.0500</td>\n",
       "      <td>NaN</td>\n",
       "      <td>S</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   PassengerId  Survived  Pclass  \\\n",
       "0            1         0       3   \n",
       "1            2         1       1   \n",
       "2            3         1       3   \n",
       "3            4         1       1   \n",
       "4            5         0       3   \n",
       "\n",
       "                                                Name     Sex   Age  SibSp  \\\n",
       "0                            Braund, Mr. Owen Harris    male  22.0      1   \n",
       "1  Cumings, Mrs. John Bradley (Florence Briggs Th...  female  38.0      1   \n",
       "2                             Heikkinen, Miss. Laina  female  26.0      0   \n",
       "3       Futrelle, Mrs. Jacques Heath (Lily May Peel)  female  35.0      1   \n",
       "4                           Allen, Mr. William Henry    male  35.0      0   \n",
       "\n",
       "   Parch            Ticket     Fare Cabin Embarked  \n",
       "0      0         A/5 21171   7.2500   NaN        S  \n",
       "1      0          PC 17599  71.2833   C85        C  \n",
       "2      0  STON/O2. 3101282   7.9250   NaN        S  \n",
       "3      0            113803  53.1000  C123        S  \n",
       "4      0            373450   8.0500   NaN        S  "
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style>\n",
       "    .dataframe thead tr:only-child th {\n",
       "        text-align: right;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: left;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>PassengerId</th>\n",
       "      <th>Survived</th>\n",
       "      <th>Pclass</th>\n",
       "      <th>Name</th>\n",
       "      <th>Sex</th>\n",
       "      <th>Age</th>\n",
       "      <th>SibSp</th>\n",
       "      <th>Parch</th>\n",
       "      <th>Ticket</th>\n",
       "      <th>Fare</th>\n",
       "      <th>Cabin</th>\n",
       "      <th>Embarked</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>886</th>\n",
       "      <td>887</td>\n",
       "      <td>0</td>\n",
       "      <td>2</td>\n",
       "      <td>Montvila, Rev. Juozas</td>\n",
       "      <td>male</td>\n",
       "      <td>27.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>211536</td>\n",
       "      <td>13.00</td>\n",
       "      <td>NaN</td>\n",
       "      <td>S</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>887</th>\n",
       "      <td>888</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>Graham, Miss. Margaret Edith</td>\n",
       "      <td>female</td>\n",
       "      <td>19.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>112053</td>\n",
       "      <td>30.00</td>\n",
       "      <td>B42</td>\n",
       "      <td>S</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>888</th>\n",
       "      <td>889</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>Johnston, Miss. Catherine Helen \"Carrie\"</td>\n",
       "      <td>female</td>\n",
       "      <td>NaN</td>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "      <td>W./C. 6607</td>\n",
       "      <td>23.45</td>\n",
       "      <td>NaN</td>\n",
       "      <td>S</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>889</th>\n",
       "      <td>890</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>Behr, Mr. Karl Howell</td>\n",
       "      <td>male</td>\n",
       "      <td>26.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>111369</td>\n",
       "      <td>30.00</td>\n",
       "      <td>C148</td>\n",
       "      <td>C</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>890</th>\n",
       "      <td>891</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>Dooley, Mr. Patrick</td>\n",
       "      <td>male</td>\n",
       "      <td>32.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>370376</td>\n",
       "      <td>7.75</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Q</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     PassengerId  Survived  Pclass                                      Name  \\\n",
       "886          887         0       2                     Montvila, Rev. Juozas   \n",
       "887          888         1       1              Graham, Miss. Margaret Edith   \n",
       "888          889         0       3  Johnston, Miss. Catherine Helen \"Carrie\"   \n",
       "889          890         1       1                     Behr, Mr. Karl Howell   \n",
       "890          891         0       3                       Dooley, Mr. Patrick   \n",
       "\n",
       "        Sex   Age  SibSp  Parch      Ticket   Fare Cabin Embarked  \n",
       "886    male  27.0      0      0      211536  13.00   NaN        S  \n",
       "887  female  19.0      0      0      112053  30.00   B42        S  \n",
       "888  female   NaN      1      2  W./C. 6607  23.45   NaN        S  \n",
       "889    male  26.0      0      0      111369  30.00  C148        C  \n",
       "890    male  32.0      0      0      370376   7.75   NaN        Q  "
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.tail()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Check Data\n",
    "1. It is hard to review a large dataset, however reviewing a few samples from a smaller dataset may just tell something. For example, Variable Name may contain errors as there are several ways used to describe a name.\n",
    "2. Check which variables contains null values. It is obvious that variables Cabin, Age and Embarked contain null values. Additionaly, variables Cabin contains the largest number of null values, while Emabrked contains the least number.\n",
    "3. About data types, seven variables are integer or floats and five variables are strings."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 891 entries, 0 to 890\n",
      "Data columns (total 12 columns):\n",
      "PassengerId    891 non-null int64\n",
      "Survived       891 non-null int64\n",
      "Pclass         891 non-null int64\n",
      "Name           891 non-null object\n",
      "Sex            891 non-null object\n",
      "Age            714 non-null float64\n",
      "SibSp          891 non-null int64\n",
      "Parch          891 non-null int64\n",
      "Ticket         891 non-null object\n",
      "Fare           891 non-null float64\n",
      "Cabin          204 non-null object\n",
      "Embarked       889 non-null object\n",
      "dtypes: float64(2), int64(5), object(5)\n",
      "memory usage: 66.2+ KB\n"
     ]
    }
   ],
   "source": [
    "data.info()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "##### To deal with the null values, \n",
    "1. Firstly, treat the variable Cabin where the null values do not mean missing data. The null values in the variable means zero. Thus, replace the null value with zero.\n",
    "2. Treat the variable Age where the null values mean missing data. The size of the missing data is large, thus use 'ffill' method to replace the null values.\n",
    "3. Treat the variable Embarked where the null values mean missing data. The size of the missing data is small, thus drop the null values directly."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\ProgramData\\Anaconda2\\lib\\site-packages\\ipykernel_launcher.py:1: SettingWithCopyWarning: \n",
      "A value is trying to be set on a copy of a slice from a DataFrame\n",
      "\n",
      "See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy\n",
      "  \"\"\"Entry point for launching an IPython kernel.\n"
     ]
    }
   ],
   "source": [
    "data['Cabin'][data['Cabin'].notnull()]=1\n",
    "data['Cabin'].fillna(0,inplace=True)\n",
    "data['Age'].fillna(method='ffill',inplace=True)\n",
    "data.dropna(inplace=True)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Structure Data\n",
    "According to the data, there are 12 variables.  \n",
    "Among these variables, I classify them into four categories.  \n",
    "Nominal categorical variables: PassengerId, Survived, Name, Sex, Ticket, Cabin, Embarked  \n",
    "Ordinal categorical variables: Pclass  \n",
    "Continous numerical variables: Age, Fare  \n",
    "Discrete numerical variables: SibSp, Parch  \n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Describe Data\n",
    "1. Total samples are 891.  \n",
    "2. Around 38.4% people survived in this sample.\n",
    "3. Most passengers (> 76%) did not travel with parents or children.\n",
    "4. Nearly 31% of the passengers had siblings and/or spouse aboard.\n",
    "5. Fares varied significantly with few passengers (<1%) paying as high as $512.\n",
    "6. Few elderly passengers (<1%) within age range 65-80."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style>\n",
       "    .dataframe thead tr:only-child th {\n",
       "        text-align: right;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: left;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>PassengerId</th>\n",
       "      <th>Survived</th>\n",
       "      <th>Pclass</th>\n",
       "      <th>Age</th>\n",
       "      <th>SibSp</th>\n",
       "      <th>Parch</th>\n",
       "      <th>Fare</th>\n",
       "      <th>Cabin</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>889.000000</td>\n",
       "      <td>889.000000</td>\n",
       "      <td>889.000000</td>\n",
       "      <td>889.000000</td>\n",
       "      <td>889.000000</td>\n",
       "      <td>889.000000</td>\n",
       "      <td>889.000000</td>\n",
       "      <td>889.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>446.000000</td>\n",
       "      <td>0.382452</td>\n",
       "      <td>2.311586</td>\n",
       "      <td>29.535624</td>\n",
       "      <td>0.524184</td>\n",
       "      <td>0.382452</td>\n",
       "      <td>32.096681</td>\n",
       "      <td>0.227222</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>256.998173</td>\n",
       "      <td>0.486260</td>\n",
       "      <td>0.834700</td>\n",
       "      <td>14.527483</td>\n",
       "      <td>1.103705</td>\n",
       "      <td>0.806761</td>\n",
       "      <td>49.697504</td>\n",
       "      <td>0.419273</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.420000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>224.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>2.000000</td>\n",
       "      <td>20.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>7.895800</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>446.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>3.000000</td>\n",
       "      <td>28.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>14.454200</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>668.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>3.000000</td>\n",
       "      <td>38.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>31.000000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>891.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>3.000000</td>\n",
       "      <td>80.000000</td>\n",
       "      <td>8.000000</td>\n",
       "      <td>6.000000</td>\n",
       "      <td>512.329200</td>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "       PassengerId    Survived      Pclass         Age       SibSp  \\\n",
       "count   889.000000  889.000000  889.000000  889.000000  889.000000   \n",
       "mean    446.000000    0.382452    2.311586   29.535624    0.524184   \n",
       "std     256.998173    0.486260    0.834700   14.527483    1.103705   \n",
       "min       1.000000    0.000000    1.000000    0.420000    0.000000   \n",
       "25%     224.000000    0.000000    2.000000   20.000000    0.000000   \n",
       "50%     446.000000    0.000000    3.000000   28.000000    0.000000   \n",
       "75%     668.000000    1.000000    3.000000   38.000000    1.000000   \n",
       "max     891.000000    1.000000    3.000000   80.000000    8.000000   \n",
       "\n",
       "            Parch        Fare       Cabin  \n",
       "count  889.000000  889.000000  889.000000  \n",
       "mean     0.382452   32.096681    0.227222  \n",
       "std      0.806761   49.697504    0.419273  \n",
       "min      0.000000    0.000000    0.000000  \n",
       "25%      0.000000    7.895800    0.000000  \n",
       "50%      0.000000   14.454200    0.000000  \n",
       "75%      0.000000   31.000000    0.000000  \n",
       "max      6.000000  512.329200    1.000000  "
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0    676\n",
       "1    118\n",
       "2     80\n",
       "5      5\n",
       "3      5\n",
       "4      4\n",
       "6      1\n",
       "Name: Parch, dtype: int64"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data['Parch'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.75869809203142535"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data['Parch'].value_counts()[0]/891.0"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0    606\n",
       "1    209\n",
       "2     28\n",
       "4     18\n",
       "3     16\n",
       "8      7\n",
       "5      5\n",
       "Name: SibSp, dtype: int64"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data['SibSp'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.31986531986531985"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "1-data['SibSp'].value_counts()[0]/891.0"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style>\n",
       "    .dataframe thead tr:only-child th {\n",
       "        text-align: right;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: left;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>PassengerId</th>\n",
       "      <th>Survived</th>\n",
       "      <th>Pclass</th>\n",
       "      <th>Age</th>\n",
       "      <th>SibSp</th>\n",
       "      <th>Parch</th>\n",
       "      <th>Fare</th>\n",
       "      <th>Cabin</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>889.000000</td>\n",
       "      <td>889.000000</td>\n",
       "      <td>889.000000</td>\n",
       "      <td>889.000000</td>\n",
       "      <td>889.000000</td>\n",
       "      <td>889.000000</td>\n",
       "      <td>889.000000</td>\n",
       "      <td>889.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>446.000000</td>\n",
       "      <td>0.382452</td>\n",
       "      <td>2.311586</td>\n",
       "      <td>29.535624</td>\n",
       "      <td>0.524184</td>\n",
       "      <td>0.382452</td>\n",
       "      <td>32.096681</td>\n",
       "      <td>0.227222</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>256.998173</td>\n",
       "      <td>0.486260</td>\n",
       "      <td>0.834700</td>\n",
       "      <td>14.527483</td>\n",
       "      <td>1.103705</td>\n",
       "      <td>0.806761</td>\n",
       "      <td>49.697504</td>\n",
       "      <td>0.419273</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.420000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>10%</th>\n",
       "      <td>90.800000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>11.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>7.550000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>20%</th>\n",
       "      <td>179.600000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>19.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>7.854200</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>30%</th>\n",
       "      <td>268.400000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>2.000000</td>\n",
       "      <td>22.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>8.050000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>40%</th>\n",
       "      <td>357.200000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>2.000000</td>\n",
       "      <td>25.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>10.500000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>446.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>3.000000</td>\n",
       "      <td>28.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>14.454200</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>60%</th>\n",
       "      <td>534.800000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>3.000000</td>\n",
       "      <td>32.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>21.075000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>70%</th>\n",
       "      <td>623.600000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>3.000000</td>\n",
       "      <td>36.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>26.820000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>80%</th>\n",
       "      <td>712.400000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>3.000000</td>\n",
       "      <td>41.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>39.687500</td>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>90%</th>\n",
       "      <td>801.200000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>3.000000</td>\n",
       "      <td>50.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>2.000000</td>\n",
       "      <td>77.287500</td>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>99%</th>\n",
       "      <td>882.120000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>3.000000</td>\n",
       "      <td>65.000000</td>\n",
       "      <td>5.000000</td>\n",
       "      <td>4.000000</td>\n",
       "      <td>249.303304</td>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>891.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>3.000000</td>\n",
       "      <td>80.000000</td>\n",
       "      <td>8.000000</td>\n",
       "      <td>6.000000</td>\n",
       "      <td>512.329200</td>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "       PassengerId    Survived      Pclass         Age       SibSp  \\\n",
       "count   889.000000  889.000000  889.000000  889.000000  889.000000   \n",
       "mean    446.000000    0.382452    2.311586   29.535624    0.524184   \n",
       "std     256.998173    0.486260    0.834700   14.527483    1.103705   \n",
       "min       1.000000    0.000000    1.000000    0.420000    0.000000   \n",
       "10%      90.800000    0.000000    1.000000   11.000000    0.000000   \n",
       "20%     179.600000    0.000000    1.000000   19.000000    0.000000   \n",
       "30%     268.400000    0.000000    2.000000   22.000000    0.000000   \n",
       "40%     357.200000    0.000000    2.000000   25.000000    0.000000   \n",
       "50%     446.000000    0.000000    3.000000   28.000000    0.000000   \n",
       "60%     534.800000    0.000000    3.000000   32.000000    0.000000   \n",
       "70%     623.600000    1.000000    3.000000   36.000000    1.000000   \n",
       "80%     712.400000    1.000000    3.000000   41.000000    1.000000   \n",
       "90%     801.200000    1.000000    3.000000   50.000000    1.000000   \n",
       "99%     882.120000    1.000000    3.000000   65.000000    5.000000   \n",
       "max     891.000000    1.000000    3.000000   80.000000    8.000000   \n",
       "\n",
       "            Parch        Fare       Cabin  \n",
       "count  889.000000  889.000000  889.000000  \n",
       "mean     0.382452   32.096681    0.227222  \n",
       "std      0.806761   49.697504    0.419273  \n",
       "min      0.000000    0.000000    0.000000  \n",
       "10%      0.000000    7.550000    0.000000  \n",
       "20%      0.000000    7.854200    0.000000  \n",
       "30%      0.000000    8.050000    0.000000  \n",
       "40%      0.000000   10.500000    0.000000  \n",
       "50%      0.000000   14.454200    0.000000  \n",
       "60%      0.000000   21.075000    0.000000  \n",
       "70%      0.000000   26.820000    0.000000  \n",
       "80%      1.000000   39.687500    1.000000  \n",
       "90%      2.000000   77.287500    1.000000  \n",
       "99%      4.000000  249.303304    1.000000  \n",
       "max      6.000000  512.329200    1.000000  "
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.describe([.1, .2, .3, .4, .5, .6, .7, .8, .9, .99])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "7. There is no repeat name in the sample.\n",
    "8. There are 64.8% male in the sample.\n",
    "9. Several passengers shared the same cabin because the cabin values have several dupicates across samples.\n",
    "10. Embarked takes three possible values. Southampton port used by most passengers\n",
    "11. Ticket feature has high ratio (22%) of duplicate values. This result is similar to that most passengers (> 76%) did not travel with parents or children, which means that probably who travels with parents or children shared same ticket number."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style>\n",
       "    .dataframe thead tr:only-child th {\n",
       "        text-align: right;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: left;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Name</th>\n",
       "      <th>Sex</th>\n",
       "      <th>Ticket</th>\n",
       "      <th>Embarked</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>889</td>\n",
       "      <td>889</td>\n",
       "      <td>889</td>\n",
       "      <td>889</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>unique</th>\n",
       "      <td>889</td>\n",
       "      <td>2</td>\n",
       "      <td>680</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>top</th>\n",
       "      <td>Graham, Mr. George Edward</td>\n",
       "      <td>male</td>\n",
       "      <td>CA. 2343</td>\n",
       "      <td>S</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>freq</th>\n",
       "      <td>1</td>\n",
       "      <td>577</td>\n",
       "      <td>7</td>\n",
       "      <td>644</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                             Name   Sex    Ticket Embarked\n",
       "count                         889   889       889      889\n",
       "unique                        889     2       680        3\n",
       "top     Graham, Mr. George Edward  male  CA. 2343        S\n",
       "freq                            1   577         7      644"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.describe(include=['O'])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Explore Data\n",
    "According to the correlation analysis, \n",
    "1. It is obvious that variables Pclass, Sex, Fare, Cabin and Embarked have a relationship with Survived.\n",
    "2. It is obvious that Fare and Pclass have a direct relationship.\n",
    "3. It is surprised that the correlation coefficient between Cabin and Survived is not 1, intuitively, who used cabin must survived, which means that there were some people survived without using Cabin.\n",
    "4. Additionally, it is interesting that there is a relationship between Embarked and Survived."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "data['Sex'].replace(to_replace=dict(female=1, male=0), inplace=True)\n",
    "data['Embarked'].replace(to_replace=dict(S=1, C=2,Q=3), inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style>\n",
       "    .dataframe thead tr:only-child th {\n",
       "        text-align: right;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: left;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>PassengerId</th>\n",
       "      <th>Survived</th>\n",
       "      <th>Pclass</th>\n",
       "      <th>Sex</th>\n",
       "      <th>Age</th>\n",
       "      <th>SibSp</th>\n",
       "      <th>Parch</th>\n",
       "      <th>Fare</th>\n",
       "      <th>Cabin</th>\n",
       "      <th>Embarked</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>889.000000</td>\n",
       "      <td>889.000000</td>\n",
       "      <td>889.000000</td>\n",
       "      <td>889.000000</td>\n",
       "      <td>889.000000</td>\n",
       "      <td>889.000000</td>\n",
       "      <td>889.000000</td>\n",
       "      <td>889.000000</td>\n",
       "      <td>889.000000</td>\n",
       "      <td>889.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>446.000000</td>\n",
       "      <td>0.382452</td>\n",
       "      <td>2.311586</td>\n",
       "      <td>0.350956</td>\n",
       "      <td>29.535624</td>\n",
       "      <td>0.524184</td>\n",
       "      <td>0.382452</td>\n",
       "      <td>32.096681</td>\n",
       "      <td>0.227222</td>\n",
       "      <td>1.362205</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>256.998173</td>\n",
       "      <td>0.486260</td>\n",
       "      <td>0.834700</td>\n",
       "      <td>0.477538</td>\n",
       "      <td>14.527483</td>\n",
       "      <td>1.103705</td>\n",
       "      <td>0.806761</td>\n",
       "      <td>49.697504</td>\n",
       "      <td>0.419273</td>\n",
       "      <td>0.636157</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.420000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>224.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>2.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>20.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>7.895800</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>446.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>3.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>28.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>14.454200</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>668.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>3.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>38.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>31.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>2.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>891.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>3.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>80.000000</td>\n",
       "      <td>8.000000</td>\n",
       "      <td>6.000000</td>\n",
       "      <td>512.329200</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>3.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "       PassengerId    Survived      Pclass         Sex         Age  \\\n",
       "count   889.000000  889.000000  889.000000  889.000000  889.000000   \n",
       "mean    446.000000    0.382452    2.311586    0.350956   29.535624   \n",
       "std     256.998173    0.486260    0.834700    0.477538   14.527483   \n",
       "min       1.000000    0.000000    1.000000    0.000000    0.420000   \n",
       "25%     224.000000    0.000000    2.000000    0.000000   20.000000   \n",
       "50%     446.000000    0.000000    3.000000    0.000000   28.000000   \n",
       "75%     668.000000    1.000000    3.000000    1.000000   38.000000   \n",
       "max     891.000000    1.000000    3.000000    1.000000   80.000000   \n",
       "\n",
       "            SibSp       Parch        Fare       Cabin    Embarked  \n",
       "count  889.000000  889.000000  889.000000  889.000000  889.000000  \n",
       "mean     0.524184    0.382452   32.096681    0.227222    1.362205  \n",
       "std      1.103705    0.806761   49.697504    0.419273    0.636157  \n",
       "min      0.000000    0.000000    0.000000    0.000000    1.000000  \n",
       "25%      0.000000    0.000000    7.895800    0.000000    1.000000  \n",
       "50%      0.000000    0.000000   14.454200    0.000000    1.000000  \n",
       "75%      1.000000    0.000000   31.000000    0.000000    2.000000  \n",
       "max      8.000000    6.000000  512.329200    1.000000    3.000000  "
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style>\n",
       "    .dataframe thead tr:only-child th {\n",
       "        text-align: right;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: left;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>PassengerId</th>\n",
       "      <th>Survived</th>\n",
       "      <th>Pclass</th>\n",
       "      <th>Sex</th>\n",
       "      <th>Age</th>\n",
       "      <th>SibSp</th>\n",
       "      <th>Parch</th>\n",
       "      <th>Fare</th>\n",
       "      <th>Cabin</th>\n",
       "      <th>Embarked</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>PassengerId</th>\n",
       "      <td>1.000000</td>\n",
       "      <td>-0.005028</td>\n",
       "      <td>-0.035330</td>\n",
       "      <td>-0.043136</td>\n",
       "      <td>0.024020</td>\n",
       "      <td>-0.057686</td>\n",
       "      <td>-0.001657</td>\n",
       "      <td>0.012703</td>\n",
       "      <td>0.020045</td>\n",
       "      <td>-0.030555</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Survived</th>\n",
       "      <td>-0.005028</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>-0.335549</td>\n",
       "      <td>0.541585</td>\n",
       "      <td>-0.069907</td>\n",
       "      <td>-0.034040</td>\n",
       "      <td>0.083151</td>\n",
       "      <td>0.255290</td>\n",
       "      <td>0.313435</td>\n",
       "      <td>0.108669</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Pclass</th>\n",
       "      <td>-0.035330</td>\n",
       "      <td>-0.335549</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>-0.127741</td>\n",
       "      <td>-0.287864</td>\n",
       "      <td>0.081656</td>\n",
       "      <td>0.016824</td>\n",
       "      <td>-0.548193</td>\n",
       "      <td>-0.723815</td>\n",
       "      <td>0.043835</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Sex</th>\n",
       "      <td>-0.043136</td>\n",
       "      <td>0.541585</td>\n",
       "      <td>-0.127741</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>-0.063014</td>\n",
       "      <td>0.116348</td>\n",
       "      <td>0.247508</td>\n",
       "      <td>0.179958</td>\n",
       "      <td>0.135589</td>\n",
       "      <td>0.118593</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Age</th>\n",
       "      <td>0.024020</td>\n",
       "      <td>-0.069907</td>\n",
       "      <td>-0.287864</td>\n",
       "      <td>-0.063014</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>-0.205270</td>\n",
       "      <td>-0.164226</td>\n",
       "      <td>0.080703</td>\n",
       "      <td>0.206095</td>\n",
       "      <td>0.026344</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>SibSp</th>\n",
       "      <td>-0.057686</td>\n",
       "      <td>-0.034040</td>\n",
       "      <td>0.081656</td>\n",
       "      <td>0.116348</td>\n",
       "      <td>-0.205270</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.414542</td>\n",
       "      <td>0.160887</td>\n",
       "      <td>-0.038657</td>\n",
       "      <td>-0.060606</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Parch</th>\n",
       "      <td>-0.001657</td>\n",
       "      <td>0.083151</td>\n",
       "      <td>0.016824</td>\n",
       "      <td>0.247508</td>\n",
       "      <td>-0.164226</td>\n",
       "      <td>0.414542</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.217532</td>\n",
       "      <td>0.039101</td>\n",
       "      <td>-0.079320</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Fare</th>\n",
       "      <td>0.012703</td>\n",
       "      <td>0.255290</td>\n",
       "      <td>-0.548193</td>\n",
       "      <td>0.179958</td>\n",
       "      <td>0.080703</td>\n",
       "      <td>0.160887</td>\n",
       "      <td>0.217532</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.480425</td>\n",
       "      <td>0.063462</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Cabin</th>\n",
       "      <td>0.020045</td>\n",
       "      <td>0.313435</td>\n",
       "      <td>-0.723815</td>\n",
       "      <td>0.135589</td>\n",
       "      <td>0.206095</td>\n",
       "      <td>-0.038657</td>\n",
       "      <td>0.039101</td>\n",
       "      <td>0.480425</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.016190</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Embarked</th>\n",
       "      <td>-0.030555</td>\n",
       "      <td>0.108669</td>\n",
       "      <td>0.043835</td>\n",
       "      <td>0.118593</td>\n",
       "      <td>0.026344</td>\n",
       "      <td>-0.060606</td>\n",
       "      <td>-0.079320</td>\n",
       "      <td>0.063462</td>\n",
       "      <td>0.016190</td>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "             PassengerId  Survived    Pclass       Sex       Age     SibSp  \\\n",
       "PassengerId     1.000000 -0.005028 -0.035330 -0.043136  0.024020 -0.057686   \n",
       "Survived       -0.005028  1.000000 -0.335549  0.541585 -0.069907 -0.034040   \n",
       "Pclass         -0.035330 -0.335549  1.000000 -0.127741 -0.287864  0.081656   \n",
       "Sex            -0.043136  0.541585 -0.127741  1.000000 -0.063014  0.116348   \n",
       "Age             0.024020 -0.069907 -0.287864 -0.063014  1.000000 -0.205270   \n",
       "SibSp          -0.057686 -0.034040  0.081656  0.116348 -0.205270  1.000000   \n",
       "Parch          -0.001657  0.083151  0.016824  0.247508 -0.164226  0.414542   \n",
       "Fare            0.012703  0.255290 -0.548193  0.179958  0.080703  0.160887   \n",
       "Cabin           0.020045  0.313435 -0.723815  0.135589  0.206095 -0.038657   \n",
       "Embarked       -0.030555  0.108669  0.043835  0.118593  0.026344 -0.060606   \n",
       "\n",
       "                Parch      Fare     Cabin  Embarked  \n",
       "PassengerId -0.001657  0.012703  0.020045 -0.030555  \n",
       "Survived     0.083151  0.255290  0.313435  0.108669  \n",
       "Pclass       0.016824 -0.548193 -0.723815  0.043835  \n",
       "Sex          0.247508  0.179958  0.135589  0.118593  \n",
       "Age         -0.164226  0.080703  0.206095  0.026344  \n",
       "SibSp        0.414542  0.160887 -0.038657 -0.060606  \n",
       "Parch        1.000000  0.217532  0.039101 -0.079320  \n",
       "Fare         0.217532  1.000000  0.480425  0.063462  \n",
       "Cabin        0.039101  0.480425  1.000000  0.016190  \n",
       "Embarked    -0.079320  0.063462  0.016190  1.000000  "
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.corr()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### The relationship between Pclass and Survived"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style>\n",
       "    .dataframe thead tr:only-child th {\n",
       "        text-align: right;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: left;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Pclass</th>\n",
       "      <th>Survived</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>0.626168</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>0.472826</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3</td>\n",
       "      <td>0.242363</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Pclass  Survived\n",
       "0       1  0.626168\n",
       "1       2  0.472826\n",
       "2       3  0.242363"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data[[\"Pclass\", \"Survived\"]].groupby(['Pclass'], as_index=False).mean()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Pclass\n",
       "1    214\n",
       "2    184\n",
       "3    491\n",
       "Name: PassengerId, dtype: int64"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.groupby('Pclass')['PassengerId'].count()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAW4AAAD7CAYAAABKfn7LAAAABHNCSVQICAgIfAhkiAAAAAlwSFlz\nAAALEgAACxIB0t1+/AAAADl0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uIDIuMS4wLCBo\ndHRwOi8vbWF0cGxvdGxpYi5vcmcvpW3flQAAIABJREFUeJzt3Xl8nFW9x/HPL5M9TafpvtKUbiwd\noKyyl5YrQhD3He4IXHdRXG9U1HC5YvReQFTECwIGQRQVBAkIClKg7CLyUBahkO60pXsyk8lk5nf/\neKbQljadNDNz5pn5vV+veTXLJPNtKd+cnuec84iqYowxJjgqXAcwxhgzOFbcxhgTMFbcxhgTMFbc\nxhgTMFbcxhgTMFbcxhgTMFbcpqiIyDwRWeE6hzHFzIrb5I2IdIlIXES6RWSNiFwnIsNc59qZiJwi\nIg+IyFYRWSciC0XkjAK8bpeInJzv1zGlx4rb5Ns7VXUYcChwBHCB4zw7EJH3A78DrgcmA+OA7wDv\ndJnLmIFYcZuCUNWVwF3AHAARGZkZga8SkY0i8sddfZ2ItIrIksxo+DkRec92n5uRGR1vFpHXReS3\nmY+LiFwmImszn3tGRObs4nsLcClwkar+QlU3q2paVReq6icyz6kQkQtEZGnm+10vIuHM594yrbP9\nKFpE2kTk5szXbBWRxSJyeOZzvwL2Af6U+RfJ14f6Z2zKhxW3KQgRmQKcBvwj86FfAfXAgcBY4LLd\nfOkS4HggDFwI3CAiEzKfuwi4B2jCHy3/JPPxtwMnALOAEcCHgPW7+N6zgSnA7weI/vHM4yRgX2AY\n8NMBnr+zM4DfZHLcvu1rVfUsYBmZf5Go6g8H8T1NmbPiNvn2RxHZBDwELAQuzhTvqcCnVXWjqiZV\ndeGuvlhVf6eqqzIj4d8CLwFHZj6dBKYCE1W1V1Uf2u7jjcB+gKjq86q6ehffflTm1119bpuPAZeq\n6iuq2g18A/iwiFRm+ft/SFXvVNUU/g+rg7P8OmN2y4rb5Nu7VXWEqk5V1c+qahx/lLtBVTfu6YtF\n5N9F5GkR2ZT5ATAHGJ359NcBAR7PTEOcA6Cq9+GPbK8A1ojIVSIyfBffftsofMIuPrfNRGDpdu8v\nBSrx58Kz8dp2b8eA2kGUvjG7ZMVtXFgOjBSREQM9SUSmAlcDnwdGqeoI4Fn8skZVX1PVT6jqROBT\nwM9EZEbmcz9W1cPwp2JmAV/bxUu8mMnyvgFirMIf1W+zD9APrAF68Kd7tuUNAWMG+j3txI7mNHvF\nitsUXGba4i78om0SkSoROWEXT23AL7d1ACJyNpmLm5n3PyAikzPvbsw8NyUiR4jIUSJShV+uvUBq\nFzkU+DLwbRE5W0SGZy5GHiciV2WedhPwJRGZllnKeDHwW1XtB/6FP4JuybzWBUDNIP4o1uDPmxsz\nKFbcxpWz8OeiXwDWAufv/ARVfQ64BHgEv+QiwKLtnnIE8JiIdONf+Puiqr4KDMcfqW/En9pYD/zv\nrkKo6u/xL16egz+6XgP8N3Bb5inX4s9NPwC8iv9D4LzM124GPgv8AliJ/0NiMJuHvg9ckJkG+uog\nvs6UObEbKRhjTLDYiNsYYwLGitsYYwLGitsYYwLGitsYYwLGitsYYwLGitsYYwLGitsYYwLGitsY\nYwLGitsYYwLGitsYYwLGitsYYwLGitsYYwLGitsYYwLGitsYYwLGitsYYwLGitsYYwLGitsYYwLG\nitsYYwLGitsYYwLGitsYYwLGitsYYwLGitsYYwLGitsYYwLGitsYYwLGitsYYwLGitsYYwKm0nUA\nY4akLVwBjABGAk1APVCF/3d7+0doF++ngQTQm/k1cWHyrC3XpU7tA7YC3dseXe0t6QL+rowZkBW3\nKT5t4UagGZiaeUzizWLe+dcwILl66TTyCHD0Th/W5tbOGLAOWLXdY/VO76/qam/ZlKssxuyOFbcp\nvLZwDbAfsC87FvS2t5tcRVuuY+t38WEBGjKP5oG+vrm1M86bhb4MeAFYDDwHvNzV3tKfy7ymPImq\nus5gSlVbWPCLLgIctN2vM/GnKorOKYn2V1/Ufabl6dv3AS/hl/j2j391tbf05ek1TQmy4i5CIjIF\nuB4Yjz8Pe5WqXu421R60hSuBucCRvFnSc4BGl7EG66DeqzZvYVi4wC/bD7wMPAs8CiwC/t7V3pIs\ncA4TEFbcRUhEJgATVPUpEWkE/g68W1WfcxztTW3hYfhzwcdlHkfhTyUEliqJaYlf17jOkREHnsAv\n8UXAw13tLRvdRjLFwoo7AETkNuCnqvoXZyHawuOA43mzqA+mxK6R9GvFqhmJGya6zrEbij+tsgh4\nCFjU1d7yittIxhUr7iInIs3AA8AcVd1SsBduC4eAY4DTgRbgwIK9tiPdWvvcnMS1B7jOMQgrgU7g\n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\n",
      "text/plain": [
       "<matplotlib.figure.Figure at 0xa83bc10>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "data.groupby('Pclass')['PassengerId'].count().plot(kind='pie', autopct='%.0f%%')\n",
    "plt.title('Pclass Count')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### The relationship between Sex and Survived"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style>\n",
       "    .dataframe thead tr:only-child th {\n",
       "        text-align: right;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: left;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Sex</th>\n",
       "      <th>Survived</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0</td>\n",
       "      <td>0.188908</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1</td>\n",
       "      <td>0.740385</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Sex  Survived\n",
       "0    0  0.188908\n",
       "1    1  0.740385"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data[[\"Sex\", \"Survived\"]].groupby(['Sex'], as_index=False).mean()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Sex\n",
       "0    577\n",
       "1    312\n",
       "Name: PassengerId, dtype: int64"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.groupby('Sex')['PassengerId'].count()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\nAAAASUVORK5CYII=\n",
      "text/plain": [
       "<matplotlib.figure.Figure at 0xa85ac90>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "data.groupby('Sex')['PassengerId'].count().plot(kind='pie', autopct='%.0f%%')\n",
    "plt.title('Sex Count')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### The relationship between Embarked and Survived"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style>\n",
       "    .dataframe thead tr:only-child th {\n",
       "        text-align: right;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: left;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Embarked</th>\n",
       "      <th>Survived</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>0.336957</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>0.553571</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3</td>\n",
       "      <td>0.389610</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Embarked  Survived\n",
       "0         1  0.336957\n",
       "1         2  0.553571\n",
       "2         3  0.389610"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data[[\"Embarked\", \"Survived\"]].groupby(['Embarked'], as_index=False).mean()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Embarked\n",
       "1    644\n",
       "2    168\n",
       "3     77\n",
       "Name: PassengerId, dtype: int64"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.groupby('Embarked')['PassengerId'].count()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAW4AAAD7CAYAAABKfn7LAAAABHNCSVQICAgIfAhkiAAAAAlwSFlz\nAAALEgAACxIB0t1+/AAAADl0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uIDIuMS4wLCBo\ndHRwOi8vbWF0cGxvdGxpYi5vcmcvpW3flQAAIABJREFUeJzt3Xl8VOXZ//HPlckeloCAioIjgqhV\nQIpWLIJLrZVxe1qrdSvaaqu1rT5dfp3qUxu1tdPaVmttrba2j9bax13QwX0BBEUFkRR3dCAJCUuA\n7Pvcvz/OAQMimUlm5j5n5nq/XvMi20y+Qflyc537nCPGGJRSSvlHnu0ASimlkqPFrZRSPqPFrZRS\nPqPFrZRSPqPFrZRSPqPFrZRSPqPFrawQkf8VkV+k8PUqROSeFL1WTES+kIrXUiodtLhVwtxCaxOR\n5l6PW23nyjQROVJE5ovIVhHZLCKvishFGfi+L4rIxen+Psr7tLhVsk41xgzq9fiu7UAikp/B7zUd\neB5YAIwH9gAuA07OVAaltLhVSojIhSKyWERucleiH4rI0e7Hq0Rkg4jM2elpI0TkGRFpEpEFIrJf\nr9f7g/u8RhFZJiLH9PpchYg8KCL3iEgjcOFOWQpE5N8i8pCIFIpInoiERWS1iNSLyP0iMrzX118g\nImvcz13dx496I3CXMebXxphNxrHMGHNWr9e7REQ+cFfj80RktPvxoIiY3n/R9F5Fu79XL4nIb0Vk\ni4h8JCInu5/7JXAMcGuu/ktHfUyLW6XS54CVOKvQe4H/A47AWZmej1M6g3p9/XnA9cAIYAXwr16f\new2YAgx3X+sBESnu9fnTgQeB8t7PE5ES4FGgAzjLGNMJfB84A5gFjAa2AH9yv/4Q4DbgAvdzewD7\n7uqHE5FSYLr7fXdJRI4HfgWcBewNrHF/HxL1OeBdnN+T3wB3iogYY64GFgHf9cq/dJQ9WtwqWY+6\nK+ptj0t6fe4jY8w/jDE9wH3AGOA6Y0yHMeZpoBOnxLeJGmMWGmM6gKuB6SIyBsAYc48xpt4Y022M\n+R1QBEzs9dyXjTGPGmPixpg292NDgCeB1cBFbg6AbwNXG2Oq3e9VAZzprnzPBB7vleNnQPxTfvZh\nOH9manfz+3Me8HdjzHL39X7q/lzB3TyntzXGmL+62e/CKf89E3yuyhEZmw2qrHGGMebZT/nc+l5v\ntwEYY3b+WO8Vd9W2N4wxzSKyGWfVWyUiPwQudt83OKU8YlfP7eUooAA4x+x49bT9gEdEpHch9+AU\n4uidcrSISP2n/HxbcEp9b+CdT/ma0cDynX6uemAfoOZTntNbXa/ntooI7Ph7ppSuuJVVY7a94Y5Q\nhgPr3Hn2T3DGDcOMMeVAAyC9nrury1o+jTOmeE5Eeq9Sq4CTjTHlvR7FxpganNVz7xylOOOSTzDG\ntAIvA1/Zzc+0Ducvim2vV+a+Xg3Q4n64tNfX77Wb1/pEhCS+VmUxLW5l02wRmSEihTiz7qXGmCpg\nMNANbATyReQanBV3n4wxv8GZiT8nIttW6H8Bfrnt4KeIjBSR093PPQic0ivHdez+z8X/Ay4UkR+L\nyB7u600WkW1z7HuBi0RkiogUATe4P1fMGLMRp8DPF5GAiHwDOCCRn8u1HhiXxNerLKXFrZL12E77\nuB8ZwGvdC/wc2Ax8Fmc+DPAU8ATwHs7BvXZ2PRrZJWPM9TgHKJ91d4/8AZgHPC0iTcArOAcBMcas\nAi53s9TijEOqd/PaS4Dj3ceH7njnDmC++/nncObkD7mvdwDwtV4vcQnwY6Ae+AywJNGfy/05znR3\nnNySxPNUlhG9kYJSSvmLrriVUspntLiVUspntLiVUspntLiVUspntLiVUspntLiVUspntLiVUspn\ntLiVUspntLiVUspntLiVUspntLiVUspntLiVUspntLiVUspntLiVUspntLiVUspntLiVUspntLiV\nUspntLiVUspntLiVUspntLiVUspntLiVUspntLiVUspntLiVUspntLiVUspntLiVUspntLiVUspn\n8m0HUGogguFoMVC206N0p7fzALPTI77T+11AM9C08yMWCXVl7idSqm9ijLGdQantguGoAHsD+7q/\nbnvsBYx0HyPcX8uBQAZidfBxkW8AaoE699edH+tjkVBPBjKpHKbFrTIuGI4WAkHggF089gdKrIUb\nuDhOgb/vPt7r9fbqWCTUYTGbyhJa3Cpt3NXzAcAUYLL766HAWHLz+EocqMIp8XeAFcBy4D86jlHJ\n0OJWKeGuoicDh/NxSR8GDLaZyyc6gVU4Jb4ceAN4MxYJtVpNpTxLi1v1SzAcHQwcDRzjPo7A3yMO\nr+kB3gYWAQuABbFIqM5uJOUVWtwqIcFwdC8+LukZwCQyc2BQfew9nBJfiFPkVZbzKEu0uNUuBcPR\n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\nFlqLc3/Uf1LR8JbtMCpxWtw5IhiOTsIp8POAvSzHScqlgXlLwgX/d7TtHFmiAXgQuAdYQEWDFoAP\naXHnmGA4GgC+CFwAnAIMtpuob48VXv3SYXkf6Xy7/7qAJ3DK+jEqGtot51EDpMWdw4LhaCHOKfVn\n4Gwr9OQ44r2iC9YW6nw7Wa3A08BcnLKut5xHpZAWtwK2H9Q8AqfETwcOsZvIofPtpNQC84F5wDNU\nNOiVJrOUFrfaJfcWa6cAx+GcZm9lj7jOt3erG3gNp6yjwAqdWecGLW7Vp2A4mgdMxSnx44BjgEGZ\n+N46395BB05RLwAWAkuoaGi2G0nZoMWtkhYMR/NxxirH4dz0eBowMh3fK8fn2604+6u3FfVSPbCo\nQItbpUgwHB2LU+DbHp8Fhg/kNXNsvt0MvAmsAN5wf12ZypNhRGQMcDfOdtA4cIcx5g+pen2VOVrc\nKm2C4eg4nJX5ZJzT8CcC44GiRJ6fxfPtWpyS3lbQbwAfpHs+LSJ7A3sbY5aLyGBgGXCGMUZPvvEZ\nLW6VUe4+8iBOiR/Ex4V+IM5KcPvt2nw8344D1cBq4IOdfl1NRUOTxWzbichc4FZjzDO2s6jkaHEr\nz3D3le8DjAHGLCy8YvjYvI3jcPaXb3uMxDlpKGAhYhzYBKx3Hxt2ersO+Aj4iIqGDgv5EiYiQZy5\n+aHGmEa7aVSytLiVP1UMHQQMwdmmOGSnt4cCxTjXKe/r0QW04BwI3PZo2cXb9cCmbLgetYgMwjng\n+UtjzMO286jkaXErlUNEpAB4HHjKGPN723lU/2hxK5UjRESAu4DNxpgrbedR/afFrVSOEJEZwCKg\nEmdeD3CVMWa+vVSqP7S4lVLKZ7L+JrNKKZVttLiVUspntLiVUspntLiVUspntLiVUspntLiVUspn\ntLiVUspntLiVUspntLiVUspntLiVUspntLiVUspntLiVUspntLiVUspntLiVUspntLiVUspntLiV\nUspntLiVUspntLiVUspntLiVUspntLiVUspntLiVUspntLiVUspntLiVUspntLiVUspntLiVUspn\ntLiVUspntLiVUspntLiVUspn/j+Aq+5kPpwYJgAAAABJRU5ErkJggg==\n",
      "text/plain": [
       "<matplotlib.figure.Figure at 0xc04c210>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "data.groupby('Embarked')['PassengerId'].count().plot(kind='pie', autopct='%.0f%%')\n",
    "plt.title('Embarked Count')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### After further analysis,\n",
    "1. The survive rate of female is much higher than male.\n",
    "2. The Pclass=1 has the highest survive rate.\n",
    "3. People who embarked from Cherbourg have the highest survive rate."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Visualise Data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<seaborn.axisgrid.FacetGrid at 0xc04cc50>"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAagAAADQCAYAAABStPXYAAAABHNCSVQICAgIfAhkiAAAAAlwSFlz\nAAALEgAACxIB0t1+/AAAADl0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uIDIuMS4wLCBo\ndHRwOi8vbWF0cGxvdGxpYi5vcmcvpW3flQAAECxJREFUeJzt3X2sZHV9x/H3RxYwgsqDK1l56GJL\nQLSVh/UBqbYVm1K1QuvSQmmzNjTbP6zFVmOX+kc1tqkkjUpsMW5EXY0pD6stm7UR6QKNNg0Cguiy\nIlQprIKwVbCYRl399o85K9dldu/MvXPv/Gbm/Uomd86Zh/u9Z+93P/M759zfSVUhSVJrnjLuAiRJ\n6seAkiQ1yYCSJDXJgJIkNcmAkiQ1yYCSJDXJgBqxJG9Psj3JnUnuSPKSEb3v65JsGNF7PT6C9zg4\nyVVJ7k1yc5LVi69M6pmhPnpFki8m2Z1k7SjqmiYrxl3ANElyBvBa4LSq+kGSZwEHDfH6FVW1u99j\nVbUF2DKaSkfiIuC7VfULSc4HLgV+b8w1aQrMWB/dD7wBeOuY62iSI6jRWgXsqqofAFTVrqr6FkCS\n+7pGI8maJDd199+RZGOSzwIf60Yjz9/zhkluSnJ6kjck+Yckz+ze6ynd409L8kCSA5P8fJLPJLkt\nyeeSnNQ95/gk/5nkliTvGtHPeg6wqbu/GTgrSUb03pptM9NHVXVfVd0J/GQU7zdtDKjR+ixwbJKv\nJbk8ya8M+LrTgXOq6veBK4HfBUiyCnhOVd2254lV9RjwJWDPe/8WcF1V/QjYCLypqk6n94ns8u45\nlwEfqKoXAQ/tq4iuGe/oc3tVn6cfDTzQ1bQbeAw4csCfV9qfWeoj7Ye7+Eaoqh5PcjrwcuDXgKuS\nbKiqj87z0i1V9X/d/auB64G/ptdg1/R5/lX0dqfdCJwPXJ7kUOBlwDVzBjIHd1/PBF7f3f84vd1x\n/ep/+Tx1ztVvtOS8WVq0Gesj7YcBNWJV9WPgJuCmJF8G1gEfBXbzxIj1qXu97PtzXv/NJP+T5Jfo\nNc+f9Pk2W4C/S3IEvU+NNwCHAI9W1Sn7Km2+2pN8Dnh6n4feWlX/tte6ncCxwM4kK4BnAt+Z73tI\ng5ihPtJ+uItvhJKcmOSEOatOAf67u38fvSaAJz6F7cuVwNuAZ1bVl/d+sKoeB75Ab5fD1qr6cVV9\nD/hGkvO6WpLkhd1L/oPeJ0SAC/f1Tavq5VV1Sp9bv6baQu8/DYC1wA3lzMMagRnrI+2HATVahwKb\nktyV5E7gZOAd3WPvBC7rPl39eJ732UyvEa7ez3OuAv6g+7rHhcBFSb4EbKd3IgPAxcAbk9xCb6Qz\nClcARya5F/gLYCSn7krMUB8leVGSncB5wAeTbB/F+06L+KFXktQiR1CSpCYZUJKkJhlQkqQmGVCS\npCYta0CdffbZRe/vCLx5m9Tb2NlH3qbgNpBlDahdu3Yt57eTppJ9pFnhLj5JUpMMKElSkwwoSVKT\nDChJUpMMKElSkwwoSVKTvB7UIq3e8Ol9Pnbfu1+zjJVI0nRxBCVJapIBJUlqkgElSWqSASVJapIB\nJUlqkgElSWqSp5mzdKeK7+99F/vekjTtHEFJkppkQEmSmmRASZKaZEBJkppkQEmSmmRASZKaZEBJ\nkppkQEmSmmRASZKaZEBJkppkQEmSmmRASZKaNFBAJTksyeYkX02yI8kZSY5Icn2Se7qvhy91sdKk\ns5ekwQ06groM+ExVnQS8ENgBbAC2VdUJwLZuWdL+2UvSgOYNqCTPAF4BXAFQVT+sqkeBc4BN3dM2\nAecuVZHSNLCXpOEMMoJ6LvAI8JEktyf5UJJDgKOq6kGA7uuz+704yfoktya59ZFHHhlZ4dIEWnAv\n2UeaRYME1ArgNOADVXUq8H2G2AVRVRurak1VrVm5cuUCy5SmwoJ7yT7SLBrkiro7gZ1VdXO3vJle\nU307yaqqejDJKuDhpSpynOa7Kq40hJnuJWlY846gquoh4IEkJ3arzgLuArYA67p164Brl6RCaUrY\nS9JwBhlBAbwJ+ESSg4CvA39EL9yuTnIRcD9w3tKUKE0Ve0ka0EABVVV3AGv6PHTWaMuRppu9JA3O\nmSQkSU0yoCRJTTKgJElNMqAkSU0yoCRJTTKgJElNMqAkSU0yoCRJTTKgJElNMqAkSU0yoCRJTTKg\nJElNMqAkSU0yoCRJTTKgJElNMqAkSU0yoCRJTTKgJElNGuiS71p+qzd8ep+P3ffu1yxjJZI0Ho6g\nJElNMqAkSU0yoCRJTTKgJElNMqAkSU0yoCRJTTKgJElNMqAkSU0yoCRJTTKgJElNMqAkSU0yoCRJ\nTRo4oJIckOT2JFu75eOT3JzkniRXJTlo6cqUpoN9JA1umBHUxcCOOcuXAu+tqhOA7wIXjbIwaUrZ\n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\nTTKgJElN+n+0co4TV9KM1gAAAABJRU5ErkJggg==\n",
      "text/plain": [
       "<matplotlib.figure.Figure at 0xc04c9b0>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "grid = sns.FacetGrid(data, col='Survived')\n",
    "grid.map(plt.hist, 'Age', bins=20)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<seaborn.axisgrid.FacetGrid at 0xc320f90>"
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\nRK5CYII=\n",
      "text/plain": [
       "<matplotlib.figure.Figure at 0xc04ccf0>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "grid = sns.FacetGrid(data, col='Survived', row='Pclass', size=2.5, aspect=1.8)\n",
    "grid.map(plt.hist, 'Age', alpha=.5, bins=20)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.figure.Figure at 0xc04c510>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "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\nlZIs+kBpi6XyPQAAAIClZ15Dpaq6rqr+T1VdWlUbhrZHVtWHq+rq4fURQ3tV1Vur6pqquqyqvn9H\n1vJbv/VbOfTQQ3PYYYflqU99aj71qU896HOuX78+Z5555g6oLtljjz12yHkAAAAAFsJCrKn0Q939\n1Rn7pyf5SHefWVWnD/u/nOTFSQ4efp6e5A+H1wftE5/4RD7wgQ/kM5/5TB760Ifmq1/9au644445\nvfeuu+7KLrvM/mtau3Zt1q5duyNKBAAAAFhUpjH97egk5wzb5yR52Yz2d/TEJ5PsXVWP2REfeOON\nN2bffffNQx/60CTJvvvum/322y+rV6/OV786ybs2bNiQI488Mklyxhln5OSTT84LX/jCnHjiiXn6\n05+eyy+//J7zHXnkkdm4cWPe/va359RTT82tt96a1atX59vf/naS5Jvf/GYOOOCA3HnnnfnCF76Q\no446Kk972tPy7Gc/O5///OeTJNdee22e+cxn5vDDD8+v/uqv7oivCQAAALBg5jtU6iR/XVUbq+rk\noe27u/vGJBleHzW075/k+hnv3TS0PWgvfOELc/311+cJT3hCXvva1+biiy++3/ds3LgxF154Yc49\n99wcf/zxueCCC5JMAqobbrghT3va0+7pu9dee+UpT3nKPed9//vfnxe96EXZddddc/LJJ+f3f//3\ns3Hjxvze7/1eXvva1yZJTjvttPzsz/5sLrnkkjz60Y/eEV8TAAAAYMHMd6j0rO7+/kymtp1SVc/Z\nTt/ZVqXu+3SqOrmqNlTVhs2bN8+piD322CMbN27MunXrsnLlyhx33HF5+9vfvt33rF27Nt/1Xd+V\nJHn5y1+e97znPUmSCy64IMcee+x9+h933HE5//zzkyTnnXdejjvuuNx22235h3/4hxx77LF56lOf\nmp/+6Z/OjTfemCT5+Mc/nhNOOCFJ8opXvGJO3wMAAABgZzGvayp19w3D61eq6i+SHJHky1X1mO6+\ncZje9pWh+6YkB8x4+6okN8xyznVJ1iXJmjVr7hM6bcuKFSty5JFH5sgjj8yTn/zknHPOOdlll13u\nmbJ2++2336v/wx72sHu2999//+yzzz657LLLcv755+dtb3vbfc6/du3avO51r8vNN9+cjRs35rnP\nfW6+8Y1vZO+9986ll146a02e7gYAAAAsVvM2UqmqHlZVe27ZTvLCJP83yfokrxy6vTLJhcP2+iQn\n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\n",
      "text/plain": [
       "<matplotlib.figure.Figure at 0xc087370>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.figure(figsize=(12,5))\n",
    "f,(ax1,ax2)=plt.subplots(1,2)\n",
    "f.set_size_inches((20,8))\n",
    "data.groupby(['Pclass','Survived'])['PassengerId'].count().unstack().plot(kind='bar',ax=ax1,stacked=True)\n",
    "ax1.set_title('Pclass VS Count')\n",
    "ax1.set_ylabel('Count')\n",
    "\n",
    "data.groupby('Pclass')['Survived'].mean().plot(kind='bar',ax=ax2)\n",
    "ax2.set_title('Pclass VS Survival Rate')\n",
    "ax2.set_ylabel('Survival Rate')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.axes._subplots.AxesSubplot at 0xdee68b0>"
      ]
     },
     "execution_count": 35,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "text/plain": [
       "<matplotlib.figure.Figure at 0xce83970>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<matplotlib.figure.Figure at 0xcdd07d0>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.figure(figsize=(14,5))\n",
    "f,(ax1,ax2)=plt.subplots(1,2)\n",
    "ax1.set_title('Sex VS Pclass VS Count')\n",
    "ax1.set_ylabel('Number of Passenger')\n",
    "ax2.set_title('Sex VS Pclass VS Survival rate')\n",
    "ax2.set_ylabel('Survival Rate')\n",
    "f.set_size_inches((20,8))\n",
    "data.groupby(['Pclass','Sex'])['Survived'].count().unstack().plot(kind='bar',ax=ax1)\n",
    "data.groupby(['Pclass','Sex'])['Survived'].mean().unstack().plot(kind='bar',ax=ax2)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Conclusion\n",
    "Based on the analysis, we can find that what data tells us is not what stories tell us. In specific,\n",
    "1. More rich people survived than poor people if we assume the Pclass has a positive relationship with the wealth.\n",
    "2. For the survived rate, it is obvious that female have higher rate than the male. For my percepective, probably male cared female than themselves.\n",
    "\n",
    "#### Limitation\n",
    "It is obvious that there are some limitations in this report.\n",
    "1. There were an estimated 2,224 passengers and crew aboard, but in this report I just use 891 samples, which means that probably the sample cannot represent the population. To analyse whether this sample can represent the population, I need to do statistics test.\n",
    "2. I used 'ffill' method to fill the null values in the variable Age, which probably casued bias.\n",
    "3. Based on the data analysis, I found that the Pclass=1 group has the highest survived rate. I concluded that more rich people survived. But to tell the truth, the first-class room is much closer to escape cabins, which probably is the true factors that affects survive rate."
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 2",
   "language": "python",
   "name": "python2"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 2
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython2",
   "version": "2.7.14"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
