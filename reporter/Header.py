
import datetime
import warnings
today = datetime.date.today()

def header (authors, Place="Paris"): # Paris est la valeur pa défaut
    """Creates the header text base on authors names
    
    Parameters
    ----------
    authorsf : a list of dictionnaries 
        each dict should have "firstname" and "lastname" keys
        
    Returns
    -------
    header_txt : str
        the header txt
    
    Note
    ----
    Data is updated at the function execution time
    
    """
    authorsf = [f'{Place}, le {today.day:02d}/{today.month:02d}/{today.year}\n\n### Auteurs :']

    for aut in authors:
        try:
            author_list = (f' - {aut["Firstname"]} {aut["Lastname"]}')
        except:
            author_list = (f' - {aut["Lastname"]}')
            warnings.warn('Firstname missing')
        authorsf.append(author_list)
    return  "\n".join(authorsf)  