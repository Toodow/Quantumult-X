import twint

c = twint.Config()

c.Username = "HighwaysYORKS"
# c.Custom["tweet"] = ["id"]
# c.Custom["user"] = ["bio"]
c.Limit = 2000
c.Store_txt = True
c.Output = "F:\\python\\TWINT\\E\\HighwaysYORKS.txt"

twint.run.Search(c)
