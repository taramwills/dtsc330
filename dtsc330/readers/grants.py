import pandas as pd

class Grants(): # Class names in pthon 
    def __init__(self, path: str):
        """Create and parse a Grants fuke
        
        Args:
            path (str): the location of the file on the disk
        """
        # What is self?
        # "Self is the specific instance of the object"
        # Store shared variables in self
        self.path = path
        self.df = self._parse(path)

    def _parse(self, path: str):
        """Parse a grants file"""
        df = pd.read_csv(path, compression = 'zip')

        mapper = {
            'APPLICATION_ID': 'application_id',
            'BUDGET_START': 'start_at', # _at means a date
            'ACTIVITY': 'grant_type',
            'TOTAL_COST': 'total_cost',
            'PI_NAMEs': 'pi_names',
            'ORG_NAME': 'organization',
            'ORG_CITY': 'city',
            'ORG_STATE': 'state',
            'ORG_COUNTRY': 'country'
            }
        
        # Make column names lowercase
        # Maybe combine for budget duration
        df = df.rename(columns = mapper)[mapper.values()]

        return df
    
    def get(self):
        """Get parsed grants"""
        return self.df

if __name__ == '__main__':
    # This is for debugging
    grants = Grants('data/RePORTER_PRJ_C_FY2025.zip')