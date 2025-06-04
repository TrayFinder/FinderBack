from dotenv import load_dotenv


def load_env_variables(file_name: str):
    """
    Load enviroment variables based on a '.env' file.

    Parameters: file_name (str): name of the env file to load from.
    """
    load_dotenv(dotenv_path=file_name, verbose=True)
