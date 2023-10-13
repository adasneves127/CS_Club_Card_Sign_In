import mysql.connector

class conn:
    def __init__(self, host: str, user: str, password: str):
        self.db = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database="csclub"
        )
        self.cursor = self.db.cursor()
        
    def create_card(self, cardID: int, first_name: str, lastName: str, bannerID: int, emailID: str, addedBy: str):
        """Create a new User in the database"""
        query = "INSERT INTO members (cardID, firstName, lastName, bannerID, emailID, addedBy) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (cardID, first_name, lastName, bannerID, emailID, addedBy)
        self.cursor.execute(query, values)
        self.db.commit()
        return self.cursor.rowcount

    def get_card_data(self, cardID: int):
        """Get the card data from the database"""
        query = "SELECT * FROM members WHERE cardID = %s"
        values = (cardID,)
        self.cursor.execute(query, values)
        return self.cursor.fetchall()
    
    def get_all_user_data(self):
        """Get all member data (Except memberID) from the database"""
        query = "SELECT firstName, lastName, emailID, bannerID FROM members"
        self.cursor.execute(query)
        return self.cursor.fetchall()
    
    def get_officer_data(self, cardID: int):
        """Get the card data from the database"""
        query = "select a.memberID, b.firstName, b.lastName, b.emailID, c.roleName from officers a, members b, roles c where a.memberID = b.cardID and a.isActive = 'yes' and c.roleID = a.role AND b.cardID = %s"
        values = (cardID,)
        self.cursor.execute(query, values)
        return self.cursor.fetchall()

    def get_all_officer_data(self):
        """Get the card data from the database"""
        query = "select b.firstName, b.lastName, b.emailID, c.roleName from officers a, members b, roles c where a.memberID = b.cardID and a.role = c.roleID and a.isActive = 'yes'"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def is_card_officer(self, cardID: int):
        """Check if the card is an officer"""
        query = "SELECT * FROM officers WHERE memberID = %s"
        values = (cardID,)
        self.cursor.execute(query, values)
        return len(self.cursor.fetchall()) > 0
    
    def appoint_officer(self, cardID: int, role: str, addedBy: int):
        """Appoint a new officer"""
        if not self.is_card_officer(addedBy):
            raise Exception("Only officers can appoint other officers!")
        roles = ['Advisor, Vice President', 'President', 'Secretary', 'Treasurer']
        if role not in ['President', 'Vice President', 'Secretary', 'Treasurer', 'Advisor']:
            raise Exception("Invalid role!")
        
        # Check that our authority is greater than the person we are appointing
        query = "SELECT role FROM officers WHERE memberID = %s"
        values = (addedBy,)
        self.cursor.execute(query, values)
        our_role = int(self.cursor.fetchall()[0][0])
        target_role = roles.index(role)
        if our_role >= target_role:
            raise Exception(f"""You do not have permission to appoint this role!
                            Your authority level: {our_role}, Target authority level: {target_role}""")
        
        
        query = "INSERT INTO officers (memberID, role, isActive, addedBy) VALUES (%s, %s, %s, %s)"
        values = (cardID, role, 'yes', addedBy)
        self.cursor.execute(query, values)
        self.db.commit()
        return self.cursor.rowcount
    
    def get_card_data_by_bannerID(self, bannerID: int):
        """Get the card data from the database"""
        query = "SELECT * FROM members WHERE bannerID = %s and isActive = 'yes'"
        values = (bannerID,)
        self.cursor.execute(query, values)
        return self.cursor.fetchall()
    
    def sign_in(self, cardID: int):
        """Sign in a member"""
        query = "INSERT INTO sign_in (memberID) VALUES (%s)"
        values = (cardID,)
        self.cursor.execute(query, values)
        self.db.commit()
        
        # set the member to active
        query = "UPDATE members SET isActive = 'yes' WHERE cardID = %s"
        values = (cardID,)
        self.cursor.execute(query, values)
        self.db.commit()
        return self.cursor.rowcount
    
    def search_user_last_name(self, last_name: str):
        """Get users where last name is like what is provided."""
        query = "SELECT firstName, lastName, emailID, bannerID FROM members WHERE isActive='yes' and lastName LIKE %s"
        values = (f"%{last_name}%",)
        self.cursor.execute(query, values)
        return self.cursor.fetchall()
    
    def deactivate_member(self,bannerID):
        query = "UPDATE members SET isActive = 'no' WHERE bannerID = %s"
        values = (int(bannerID),)
        self.cursor.execute(query, values)
        self.db.commit()
        return self.cursor.rowcount
    
    def reactivate_member(self,bannerID):
        query = "UPDATE members SET isActive = 'yes' WHERE bannerID = %s"
        values = (int(bannerID),)
        self.cursor.execute(query, values)
        self.db.commit()
        return self.cursor.rowcount
    
    def update_user(self, card_id, col, data):
        query = f"UPDATE members SET `{col}`" +  "= %s WHERE cardID = %s"
        values = (data, card_id)
        self.cursor.execute(query, values)
        self.db.commit()
        
        
    def close(self):
        self.db.close()
        
        

        