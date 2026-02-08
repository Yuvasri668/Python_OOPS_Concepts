#Encapsulation Task

class InstagramAccount:
    def __init__(self, account_name, password):
        self.account_name = account_name
        self._private_reels = []
        self.__archived_reels = []
        self.__password = password

    def add_private_reel(self, reel_name):
        self._private_reels.append(reel_name)

    def display_private_reels(self, is_follower):
        if is_follower:
            print("Private Reels:", self._private_reels)
        else:
            print("Access Denied! Only followers can view private reels")

    def add_archived_reel(self, reel_name):
        self.__archived_reels.append(reel_name)

    def display_archived_reels(self, password):
        if password == self.__password:
            print("Archived Reels:", self.__archived_reels)
        else:
            print("Access Denied! Only account holder can view archived reels")

    def get_archived_reels(self, password):
        if password == self.__password:
            return self.__archived_reels
        else:
            return "Access Denied!"
        
    def set_password(self, old_password, new_password):
        if old_password == self.__password:
            self.__password = new_password
            print("\nPassword updated successfully")
        else:
            print("Incorrect password")

insta = InstagramAccount("Yuvasri_official", "1234")
insta.add_private_reel("Dance Reel")
insta.add_private_reel("Travel Reel")
print("Follower View")
insta.display_private_reels(True)
print("\nNon-Follower view")
insta.display_private_reels(False)
insta.add_archived_reel("Old Travel Reel")
insta.add_archived_reel("College Days")
print("\nArchived Reels (Correct Password)")
insta.display_archived_reels("1234")
print("\nArchived Reels (Wrong Password)")
insta.display_archived_reels("1230")
insta.set_password("1234", "5678")
print("\nArchived Reels (New Password)")
insta.display_archived_reels("5678")
