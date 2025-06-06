import sqlite3

# Connect to a database file (it will be created if it doesn't exist)
conn = sqlite3.connect("dev.sqlite3")
cursor = conn.cursor()

'''

d96a955c-b061-7080-194e-7e597383cad9: enquiry@thecodingfun.com

d9aa357c-20d1-704c-3877-63edc40201bd: claudia.yao2012@gmail.com

c9da252c-9041-7089-170c-be754918cc8d: e1331095@u.nus.edu

'''

# Define multiple rows of data
data = [
    ("d96a955c-b061-7080-194e-7e597383cad9", "HappyBird", "Loves gardening", 30, "1234567890", "avatar1.png"),
    ("d9aa357c-20d1-704c-3877-63edc40201bd", "CocaCola", "Enjoys hiking", 45, "0987654321", "avatar2.png"),
    ("c9da252c-9041-7089-170c-be754918cc8d", "Claudiaaaa", "Tech enthusiast", 28, "5555555555", "avatar3.png"),
]

# Insert the data into user_summary table
cursor.executemany("""
    INSERT INTO user_summary (
        user_id, nick_name, description, age, phone_number, avatar_object_key
    ) VALUES (?, ?, ?, ?, ?, ?)
""", data)


data = [
('c9da252c-9041-7089-170c-be754918cc8d', '0013_01.jpg', 'Bob Luo_lxbdw', 'watch movie together', 'best friend'),
('c9da252c-9041-7089-170c-be754918cc8d', '0029_01.jpg', 'Bob Luo_lxbdw', 'classmate in secondary school', 'best friend'),
('c9da252c-9041-7089-170c-be754918cc8d', '0058_01.jpg', 'Bob Luo_lxbdw', 'have the afternoon tea', 'best friend'),
('c9da252c-9041-7089-170c-be754918cc8d', '0070_01.jpg', 'Bob Luo_lxbdw', 'have the afternoon tea', 'best friend'),
('c9da252c-9041-7089-170c-be754918cc8d', '0137_01.jpg', 'Bob Luo_lxbdw', 'at the birthday party', 'best friend'),
('c9da252c-9041-7089-170c-be754918cc8d', '0162_01.jpg', 'Bob Luo_lxbdw', 'walk in the park', 'nurse'),
('c9da252c-9041-7089-170c-be754918cc8d', '0170_01.jpg', 'Bob Luo_lxbdw', 'particiate in the wedding', 'best friend'),
('c9da252c-9041-7089-170c-be754918cc8d', '0234_02.jpg', 'Bob Luo_lxbdw', 'at the birthday party', 'best friend'),
('c9da252c-9041-7089-170c-be754918cc8d', '0261_01.jpg', 'Bob Luo_lxbdw', 'just enjoy the time', 'best friend'),
('c9da252c-9041-7089-170c-be754918cc8d', '0273_01.jpg', 'Bob Luo_lxbdw', 'just enjoy the time', 'best friend'),
('c9da252c-9041-7089-170c-be754918cc8d', '0310_01.jpg', 'Bob Luo_lxbdw', 'watch movie together', 'best friend'),
('c9da252c-9041-7089-170c-be754918cc8d', '0001_01.jpg', 'Catheline_ecxlz', 'just enjoy the time', 'friend'),
('c9da252c-9041-7089-170c-be754918cc8d', '0025_01.jpg', 'Catheline_ecxlz', 'visit you at the festival', 'best friend'),
('c9da252c-9041-7089-170c-be754918cc8d', '0029_02.jpg', 'Catheline_ecxlz', 'classmate in secondary school', 'friend'),
('c9da252c-9041-7089-170c-be754918cc8d', '0037_01.jpg', 'Catheline_ecxlz', 'watch movie together', 'friend'),
('c9da252c-9041-7089-170c-be754918cc8d', '0054_01.jpg', 'Catheline_ecxlz', 'university rootmate', 'colleague'),
('c9da252c-9041-7089-170c-be754918cc8d', '0070_01.jpg', 'Catheline_ecxlz', 'goint outside for dinner', 'friend'),
('c9da252c-9041-7089-170c-be754918cc8d', '0091_02.jpg', 'Catheline_ecxlz', 'goint outside for dinner', 'friend'),
('c9da252c-9041-7089-170c-be754918cc8d', '0113_01.jpg', 'Catheline_ecxlz', 'walk in the park', 'friend'),
('c9da252c-9041-7089-170c-be754918cc8d', '0137_01.jpg', 'Catheline_ecxlz', 'classmate in secondary school', 'friend'),
('c9da252c-9041-7089-170c-be754918cc8d', '0202_02.jpg', 'Catheline_ecxlz', 'visit you at the festival', 'friend'),
('c9da252c-9041-7089-170c-be754918cc8d', '0292_01.jpg', 'Catheline_ecxlz', 'goint outside for dinner', 'friend'),
('c9da252c-9041-7089-170c-be754918cc8d', '0001_01.jpg', 'Catheline_zztxa', 'goint outside for dinner', 'friend'),
('c9da252c-9041-7089-170c-be754918cc8d', '0025_01.jpg', 'Catheline_zztxa', 'watch movie together', 'daughter'),
('c9da252c-9041-7089-170c-be754918cc8d', '0037_01.jpg', 'Catheline_zztxa', 'goint outside for dinner', 'friend'),
('c9da252c-9041-7089-170c-be754918cc8d', '0054_01.jpg', 'Catheline_zztxa', 'particiate in the wedding', 'friend'),
('c9da252c-9041-7089-170c-be754918cc8d', '0113_01.jpg', 'Catheline_zztxa', 'visit you at the festival', 'friend'),
('c9da252c-9041-7089-170c-be754918cc8d', '0170_01.jpg', 'Catheline_zztxa', 'visit you at the festival', 'daughter'),
('c9da252c-9041-7089-170c-be754918cc8d', '0210_01.jpg', 'Catheline_zztxa', 'particiate in the wedding', 'friend'),
('c9da252c-9041-7089-170c-be754918cc8d', '0245_01.jpg', 'Catheline_zztxa', 'meet on the street', 'colleague'),
('c9da252c-9041-7089-170c-be754918cc8d', '0261_01.jpg', 'Catheline_zztxa', 'visit you at the festival', 'friend'),
('c9da252c-9041-7089-170c-be754918cc8d', '0280_01.jpg', 'Catheline_zztxa', 'particiate in the wedding', 'friend'),
('c9da252c-9041-7089-170c-be754918cc8d', '0302_01.jpg', 'Catheline_zztxa', 'visit you at the festival', 'son'),
('c9da252c-9041-7089-170c-be754918cc8d', '0001_01.jpg', 'David Chan_rpnby', 'visit you at the festival', 'caregiver'),
('c9da252c-9041-7089-170c-be754918cc8d', '0037_01.jpg', 'David Chan_rpnby', 'goint outside for dinner', 'caregiver'),
('c9da252c-9041-7089-170c-be754918cc8d', '0046_01.jpg', 'David Chan_rpnby', 'have the afternoon tea', 'caregiver'),
('c9da252c-9041-7089-170c-be754918cc8d', '0054_03.jpg', 'David Chan_rpnby', 'just enjoy the time', 'caregiver'),
('c9da252c-9041-7089-170c-be754918cc8d', '0062_01.jpg', 'David Chan_rpnby', 'particiate in the wedding', 'caregiver'),
('c9da252c-9041-7089-170c-be754918cc8d', '0129_01.jpg', 'David Chan_rpnby', 'university rootmate', 'caregiver'),
('c9da252c-9041-7089-170c-be754918cc8d', '0158_01.jpg', 'David Chan_rpnby', 'have the afternoon tea', 'caregiver'),
('c9da252c-9041-7089-170c-be754918cc8d', '0202_01.jpg', 'David Chan_rpnby', 'walk in the park', 'caregiver'),
('c9da252c-9041-7089-170c-be754918cc8d', '0212_01.jpg', 'David Chan_rpnby', 'walk in the park', 'caregiver'),
('c9da252c-9041-7089-170c-be754918cc8d', '0280_01.jpg', 'David Chan_rpnby', 'at the birthday party', 'caregiver'),
('c9da252c-9041-7089-170c-be754918cc8d', '0302_01.jpg', 'David Chan_rpnby', 'have the afternoon tea', 'caregiver'),
('c9da252c-9041-7089-170c-be754918cc8d', '0013_01.jpg', 'Draren_qikfi', 'university rootmate', 'son'),
('c9da252c-9041-7089-170c-be754918cc8d', '0035_01.jpg', 'Draren_qikfi', 'classmate in secondary school', 'son'),
('c9da252c-9041-7089-170c-be754918cc8d', '0044_01.jpg', 'Draren_qikfi', 'visit you at the festival', 'son'),
('c9da252c-9041-7089-170c-be754918cc8d', '0048_01.jpg', 'Draren_qikfi', 'walk in the park', 'son'),
('c9da252c-9041-7089-170c-be754918cc8d', '0054_01.jpg', 'Draren_qikfi', 'watch movie together', 'son'),
('c9da252c-9041-7089-170c-be754918cc8d', '0062_01.jpg', 'Draren_qikfi', 'particiate in the wedding', 'son'),
('c9da252c-9041-7089-170c-be754918cc8d', '0081_01.jpg', 'Draren_qikfi', 'watch movie together', 'son'),
('c9da252c-9041-7089-170c-be754918cc8d', '0125_01.jpg', 'Draren_qikfi', 'watch movie together', 'son'),
('c9da252c-9041-7089-170c-be754918cc8d', '0156_01.jpg', 'Draren_qikfi', 'visit you at the festival', 'best friend'),
('c9da252c-9041-7089-170c-be754918cc8d', '0181_01.jpg', 'Draren_qikfi', 'just enjoy the time', 'son'),
('c9da252c-9041-7089-170c-be754918cc8d', '0193_01.jpg', 'Draren_qikfi', 'have the afternoon tea', 'son'),
('c9da252c-9041-7089-170c-be754918cc8d', '0001_01.jpg', 'Mark Song_ezmao', 'at the birthday party', 'nurse'),
('c9da252c-9041-7089-170c-be754918cc8d', '0025_01.jpg', 'Mark Song_ezmao', 'classmate in secondary school', 'doctor'),
('c9da252c-9041-7089-170c-be754918cc8d', '0029_01.jpg', 'Mark Song_ezmao', 'visit you at the festival', 'nurse'),
('c9da252c-9041-7089-170c-be754918cc8d', '0083_01.jpg', 'Mark Song_ezmao', 'visit you at the festival', 'nurse'),
('c9da252c-9041-7089-170c-be754918cc8d', '0113_01.jpg', 'Mark Song_ezmao', 'walk in the park', 'nurse'),
('c9da252c-9041-7089-170c-be754918cc8d', '0125_01.jpg', 'Mark Song_ezmao', 'watch movie together', 'nurse'),
('c9da252c-9041-7089-170c-be754918cc8d', '0154_01.jpg', 'Mark Song_ezmao', 'classmate in secondary school', 'nurse'),
('c9da252c-9041-7089-170c-be754918cc8d', '0170_01.jpg', 'Mark Song_ezmao', 'just enjoy the time', 'nurse'),
('c9da252c-9041-7089-170c-be754918cc8d', '0334_01.jpg', 'Mark Song_ezmao', 'have the afternoon tea', 'daughter'),
('c9da252c-9041-7089-170c-be754918cc8d', '0345_01.jpg', 'Mark Song_ezmao', 'just enjoy the time', 'nurse'),
('c9da252c-9041-7089-170c-be754918cc8d', '0349_01.jpg', 'Mark Song_ezmao', 'watch movie together', 'son'),
('c9da252c-9041-7089-170c-be754918cc8d', '0001_01.jpg', 'Mark Song_ofgrq', 'goint outside for dinner', 'colleague'),
('c9da252c-9041-7089-170c-be754918cc8d', '0025_01.jpg', 'Mark Song_ofgrq', 'meet on the street', 'colleague'),
('c9da252c-9041-7089-170c-be754918cc8d', '0029_02.jpg', 'Mark Song_ofgrq', 'university rootmate', 'colleague'),
('c9da252c-9041-7089-170c-be754918cc8d', '0054_01.jpg', 'Mark Song_ofgrq', 'particiate in the wedding', 'colleague'),
('c9da252c-9041-7089-170c-be754918cc8d', '0058_02.jpg', 'Mark Song_ofgrq', 'classmate in secondary school', 'colleague'),
('c9da252c-9041-7089-170c-be754918cc8d', '0062_01.jpg', 'Mark Song_ofgrq', 'classmate in secondary school', 'colleague'),
('c9da252c-9041-7089-170c-be754918cc8d', '0091_01.jpg', 'Mark Song_ofgrq', 'particiate in the wedding', 'colleague'),
('c9da252c-9041-7089-170c-be754918cc8d', '0162_01.jpg', 'Mark Song_ofgrq', 'visit you at the festival', 'colleague'),
('c9da252c-9041-7089-170c-be754918cc8d', '0392_02.jpg', 'Mark Song_ofgrq', 'goint outside for dinner', 'colleague'),
('c9da252c-9041-7089-170c-be754918cc8d', '0406_01.jpg', 'Mark Song_ofgrq', 'watch movie together', 'colleague'),
('c9da252c-9041-7089-170c-be754918cc8d', '0430_01.jpg', 'Mark Song_ofgrq', 'at the birthday party', 'colleague'),
('c9da252c-9041-7089-170c-be754918cc8d', '0013_01.jpg', 'Mark Song_tornf', 'particiate in the wedding', 'daughter'),
('c9da252c-9041-7089-170c-be754918cc8d', '0037_01.jpg', 'Mark Song_tornf', 'watch movie together', 'daughter'),
('c9da252c-9041-7089-170c-be754918cc8d', '0054_01.jpg', 'Mark Song_tornf', 'visit you at the festival', 'daughter'),
('c9da252c-9041-7089-170c-be754918cc8d', '0058_01.jpg', 'Mark Song_tornf', 'meet on the street', 'daughter'),
('c9da252c-9041-7089-170c-be754918cc8d', '0154_01.jpg', 'Mark Song_tornf', 'university rootmate', 'daughter'),
('c9da252c-9041-7089-170c-be754918cc8d', '0280_01.jpg', 'Mark Song_tornf', 'particiate in the wedding', 'daughter'),
('c9da252c-9041-7089-170c-be754918cc8d', '0292_01.jpg', 'Mark Song_tornf', 'meet on the street', 'son'),
('c9da252c-9041-7089-170c-be754918cc8d', '0380_01.jpg', 'Mark Song_tornf', 'meet on the street', 'daughter'),
('c9da252c-9041-7089-170c-be754918cc8d', '0477_02.jpg', 'Mark Song_tornf', 'just enjoy the time', 'daughter'),
('c9da252c-9041-7089-170c-be754918cc8d', '0484_01.jpg', 'Mark Song_tornf', 'just enjoy the time', 'caregiver'),
('c9da252c-9041-7089-170c-be754918cc8d', '0488_01.jpg', 'Mark Song_tornf', 'classmate in secondary school', 'daughter'),
('c9da252c-9041-7089-170c-be754918cc8d', '0025_01.jpg', 'Sandra Cathe_lrjhe', 'at the birthday party', 'friend'),
('c9da252c-9041-7089-170c-be754918cc8d', '0029_01.jpg', 'Sandra Cathe_lrjhe', 'goint outside for dinner', 'friend'),
('c9da252c-9041-7089-170c-be754918cc8d', '0037_01.jpg', 'Sandra Cathe_lrjhe', 'goint outside for dinner', 'friend'),
('c9da252c-9041-7089-170c-be754918cc8d', '0046_01.jpg', 'Sandra Cathe_lrjhe', 'classmate in secondary school', 'son'),
('c9da252c-9041-7089-170c-be754918cc8d', '0062_01.jpg', 'Sandra Cathe_lrjhe', 'watch movie together', 'caregiver'),
('c9da252c-9041-7089-170c-be754918cc8d', '0083_01.jpg', 'Sandra Cathe_lrjhe', 'have the afternoon tea', 'friend'),
('c9da252c-9041-7089-170c-be754918cc8d', '0212_01.jpg', 'Sandra Cathe_lrjhe', 'visit you at the festival', 'friend'),
('c9da252c-9041-7089-170c-be754918cc8d', '0257_01.jpg', 'Sandra Cathe_lrjhe', 'meet on the street', 'friend'),
('c9da252c-9041-7089-170c-be754918cc8d', '0271_01.jpg', 'Sandra Cathe_lrjhe', 'watch movie together', 'friend'),
('c9da252c-9041-7089-170c-be754918cc8d', '0310_01.jpg', 'Sandra Cathe_lrjhe', 'university rootmate', 'friend'),
('c9da252c-9041-7089-170c-be754918cc8d', '0312_01.jpg', 'Sandra Cathe_lrjhe', 'classmate in secondary school', 'friend'),
('c9da252c-9041-7089-170c-be754918cc8d', '0046_01.jpg', 'Sean_fypgj', 'have the afternoon tea', 'best friend'),
('c9da252c-9041-7089-170c-be754918cc8d', '0058_02.jpg', 'Sean_fypgj', 'have the afternoon tea', 'best friend'),
('c9da252c-9041-7089-170c-be754918cc8d', '0081_01.jpg', 'Sean_fypgj', 'walk in the park', 'best friend'),
('c9da252c-9041-7089-170c-be754918cc8d', '0091_01.jpg', 'Sean_fypgj', 'classmate in secondary school', 'best friend'),
('c9da252c-9041-7089-170c-be754918cc8d', '0101_01.jpg', 'Sean_fypgj', 'visit you at the festival', 'best friend'),
('c9da252c-9041-7089-170c-be754918cc8d', '0125_02.jpg', 'Sean_fypgj', 'classmate in secondary school', 'best friend'),
('c9da252c-9041-7089-170c-be754918cc8d', '0146_02.jpg', 'Sean_fypgj', 'walk in the park', 'best friend'),
('c9da252c-9041-7089-170c-be754918cc8d', '0158_01.jpg', 'Sean_fypgj', 'visit you at the festival', 'best friend'),
('c9da252c-9041-7089-170c-be754918cc8d', '0181_01.jpg', 'Sean_fypgj', 'walk in the park', 'best friend'),
('c9da252c-9041-7089-170c-be754918cc8d', '0245_01.jpg', 'Sean_fypgj', 'university rootmate', 'colleague'),
('c9da252c-9041-7089-170c-be754918cc8d', '0302_01.jpg', 'Sean_fypgj', 'at the birthday party', 'best friend'),
('c9da252c-9041-7089-170c-be754918cc8d', '0007_02.jpg', 'Steve_tyhwx', 'goint outside for dinner', 'neighbour'),
('c9da252c-9041-7089-170c-be754918cc8d', '0029_01.jpg', 'Steve_tyhwx', 'just enjoy the time', 'neighbour'),
('c9da252c-9041-7089-170c-be754918cc8d', '0037_02.jpg', 'Steve_tyhwx', 'just enjoy the time', 'neighbour'),
('c9da252c-9041-7089-170c-be754918cc8d', '0046_03.jpg', 'Steve_tyhwx', 'have the afternoon tea', 'neighbour'),
('c9da252c-9041-7089-170c-be754918cc8d', '0062_02.jpg', 'Steve_tyhwx', 'meet on the street', 'neighbour'),
('c9da252c-9041-7089-170c-be754918cc8d', '0135_01.jpg', 'Steve_tyhwx', 'goint outside for dinner', 'neighbour'),
('c9da252c-9041-7089-170c-be754918cc8d', '0139_01.jpg', 'Steve_tyhwx', 'university rootmate', 'neighbour'),
('c9da252c-9041-7089-170c-be754918cc8d', '0146_03.jpg', 'Steve_tyhwx', 'watch movie together', 'neighbour'),
('c9da252c-9041-7089-170c-be754918cc8d', '0148_01.jpg', 'Steve_tyhwx', 'meet on the street', 'neighbour'),
('c9da252c-9041-7089-170c-be754918cc8d', '0158_02.jpg', 'Steve_tyhwx', 'at the birthday party', 'neighbour'),
('c9da252c-9041-7089-170c-be754918cc8d', '0243_01.jpg', 'Steve_tyhwx', 'have the afternoon tea', 'neighbour'),
('c9da252c-9041-7089-170c-be754918cc8d', '0025_01.jpg', 'Weifeng Sun_qpdxg', 'have the afternoon tea', 'best friend'),
('c9da252c-9041-7089-170c-be754918cc8d', '0027_01.jpg', 'Weifeng Sun_qpdxg', 'at the birthday party', 'best friend'),
('c9da252c-9041-7089-170c-be754918cc8d', '0037_01.jpg', 'Weifeng Sun_qpdxg', 'meet on the street', 'best friend'),
('c9da252c-9041-7089-170c-be754918cc8d', '0046_01.jpg', 'Weifeng Sun_qpdxg', 'watch movie together', 'best friend'),
('c9da252c-9041-7089-170c-be754918cc8d', '0093_01.jpg', 'Weifeng Sun_qpdxg', 'at the birthday party', 'best friend'),
('c9da252c-9041-7089-170c-be754918cc8d', '0125_01.jpg', 'Weifeng Sun_qpdxg', 'classmate in secondary school', 'best friend'),
('c9da252c-9041-7089-170c-be754918cc8d', '0158_01.jpg', 'Weifeng Sun_qpdxg', 'visit you at the festival', 'best friend'),
('c9da252c-9041-7089-170c-be754918cc8d', '0162_01.jpg', 'Weifeng Sun_qpdxg', 'university rootmate', 'best friend'),
('c9da252c-9041-7089-170c-be754918cc8d', '0170_01.jpg', 'Weifeng Sun_qpdxg', 'university rootmate', 'best friend'),
('c9da252c-9041-7089-170c-be754918cc8d', '0212_01.jpg', 'Weifeng Sun_qpdxg', 'goint outside for dinner', 'best friend'),
('c9da252c-9041-7089-170c-be754918cc8d', '0255_01.jpg', 'Weifeng Sun_qpdxg', 'walk in the park', 'daughter'),
('d96a955c-b061-7080-194e-7e597383cad9', '0013_01.jpg', 'Dave_cjois', 'watch movie together', 'doctor'),
('d96a955c-b061-7080-194e-7e597383cad9', '0025_01.jpg', 'Dave_cjois', 'walk in the park', 'doctor'),
('d96a955c-b061-7080-194e-7e597383cad9', '0037_01.jpg', 'Dave_cjois', 'visit you at the festival', 'doctor'),
('d96a955c-b061-7080-194e-7e597383cad9', '0046_01.jpg', 'Dave_cjois', 'meet on the street', 'doctor'),
('d96a955c-b061-7080-194e-7e597383cad9', '0054_01.jpg', 'Dave_cjois', 'have the afternoon tea', 'doctor'),
('d96a955c-b061-7080-194e-7e597383cad9', '0058_01.jpg', 'Dave_cjois', 'visit you at the festival', 'doctor'),
('d96a955c-b061-7080-194e-7e597383cad9', '0091_02.jpg', 'Dave_cjois', 'have the afternoon tea', 'caregiver'),
('d96a955c-b061-7080-194e-7e597383cad9', '0113_01.jpg', 'Dave_cjois', 'visit you at the festival', 'doctor'),
('d96a955c-b061-7080-194e-7e597383cad9', '0129_01.jpg', 'Dave_cjois', 'have the afternoon tea', 'doctor'),
('d96a955c-b061-7080-194e-7e597383cad9', '0170_01.jpg', 'Dave_cjois', 'particiate in the wedding', 'doctor'),
('d96a955c-b061-7080-194e-7e597383cad9', '0469_02.jpg', 'Dave_cjois', 'have the afternoon tea', 'doctor'),
('d96a955c-b061-7080-194e-7e597383cad9', '0001_01.jpg', 'David Chan_gfwlp', 'have the afternoon tea', 'colleague'),
('d96a955c-b061-7080-194e-7e597383cad9', '0046_01.jpg', 'David Chan_gfwlp', 'at the birthday party', 'colleague'),
('d96a955c-b061-7080-194e-7e597383cad9', '0058_01.jpg', 'David Chan_gfwlp', 'classmate in secondary school', 'colleague'),
('d96a955c-b061-7080-194e-7e597383cad9', '0062_01.jpg', 'David Chan_gfwlp', 'particiate in the wedding', 'best friend'),
('d96a955c-b061-7080-194e-7e597383cad9', '0137_01.jpg', 'David Chan_gfwlp', 'walk in the park', 'colleague'),
('d96a955c-b061-7080-194e-7e597383cad9', '0183_02.jpg', 'David Chan_gfwlp', 'goint outside for dinner', 'colleague'),
('d96a955c-b061-7080-194e-7e597383cad9', '0202_01.jpg', 'David Chan_gfwlp', 'watch movie together', 'colleague'),
('d96a955c-b061-7080-194e-7e597383cad9', '0280_02.jpg', 'David Chan_gfwlp', 'university rootmate', 'colleague'),
('d96a955c-b061-7080-194e-7e597383cad9', '0441_02.jpg', 'David Chan_gfwlp', 'classmate in secondary school', 'colleague'),
('d96a955c-b061-7080-194e-7e597383cad9', '0441_03.jpg', 'David Chan_gfwlp', 'just enjoy the time', 'colleague'),
('d96a955c-b061-7080-194e-7e597383cad9', '0496_01.jpg', 'David Chan_gfwlp', 'just enjoy the time', 'colleague'),
('d96a955c-b061-7080-194e-7e597383cad9', '0025_01.jpg', 'Kris Tan_qjnpm', 'meet on the street', 'daughter'),
('d96a955c-b061-7080-194e-7e597383cad9', '0029_01.jpg', 'Kris Tan_qjnpm', 'visit you at the festival', 'colleague'),
('d96a955c-b061-7080-194e-7e597383cad9', '0037_01.jpg', 'Kris Tan_qjnpm', 'just enjoy the time', 'daughter'),
('d96a955c-b061-7080-194e-7e597383cad9', '0058_01.jpg', 'Kris Tan_qjnpm', 'goint outside for dinner', 'daughter'),
('d96a955c-b061-7080-194e-7e597383cad9', '0070_01.jpg', 'Kris Tan_qjnpm', 'particiate in the wedding', 'daughter'),
('d96a955c-b061-7080-194e-7e597383cad9', '0146_01.jpg', 'Kris Tan_qjnpm', 'just enjoy the time', 'daughter'),
('d96a955c-b061-7080-194e-7e597383cad9', '0154_01.jpg', 'Kris Tan_qjnpm', 'university rootmate', 'daughter'),
('d96a955c-b061-7080-194e-7e597383cad9', '0170_01.jpg', 'Kris Tan_qjnpm', 'particiate in the wedding', 'daughter'),
('d96a955c-b061-7080-194e-7e597383cad9', '0183_03.jpg', 'Kris Tan_qjnpm', 'watch movie together', 'daughter'),
('d96a955c-b061-7080-194e-7e597383cad9', '0257_02.jpg', 'Kris Tan_qjnpm', 'just enjoy the time', 'daughter'),
('d96a955c-b061-7080-194e-7e597383cad9', '0302_02.jpg', 'Kris Tan_qjnpm', 'just enjoy the time', 'daughter'),
('d96a955c-b061-7080-194e-7e597383cad9', '0001_01.jpg', 'Sandra Lee_qwdcz', 'university rootmate', 'doctor'),
('d96a955c-b061-7080-194e-7e597383cad9', '0048_01.jpg', 'Sandra Lee_qwdcz', 'visit you at the festival', 'doctor'),
('d96a955c-b061-7080-194e-7e597383cad9', '0060_01.jpg', 'Sandra Lee_qwdcz', 'watch movie together', 'doctor'),
('d96a955c-b061-7080-194e-7e597383cad9', '0070_01.jpg', 'Sandra Lee_qwdcz', 'university rootmate', 'doctor'),
('d96a955c-b061-7080-194e-7e597383cad9', '0113_01.jpg', 'Sandra Lee_qwdcz', 'classmate in secondary school', 'doctor'),
('d96a955c-b061-7080-194e-7e597383cad9', '0125_01.jpg', 'Sandra Lee_qwdcz', 'meet on the street', 'doctor'),
('d96a955c-b061-7080-194e-7e597383cad9', '0139_01.jpg', 'Sandra Lee_qwdcz', 'walk in the park', 'doctor'),
('d96a955c-b061-7080-194e-7e597383cad9', '0144_01.jpg', 'Sandra Lee_qwdcz', 'goint outside for dinner', 'doctor'),
('d96a955c-b061-7080-194e-7e597383cad9', '0183_01.jpg', 'Sandra Lee_qwdcz', 'have the afternoon tea', 'doctor'),
('d96a955c-b061-7080-194e-7e597383cad9', '0234_01.jpg', 'Sandra Lee_qwdcz', 'goint outside for dinner', 'doctor'),
('d96a955c-b061-7080-194e-7e597383cad9', '0363_01.jpg', 'Sandra Lee_qwdcz', 'visit you at the festival', 'doctor'),
('d96a955c-b061-7080-194e-7e597383cad9', '0029_02.jpg', 'Tera_ahblx', 'meet on the street', 'neighbour'),
('d96a955c-b061-7080-194e-7e597383cad9', '0054_02.jpg', 'Tera_ahblx', 'particiate in the wedding', 'nurse'),
('d96a955c-b061-7080-194e-7e597383cad9', '0058_01.jpg', 'Tera_ahblx', 'have the afternoon tea', 'neighbour'),
('d96a955c-b061-7080-194e-7e597383cad9', '0113_01.jpg', 'Tera_ahblx', 'watch movie together', 'neighbour'),
('d96a955c-b061-7080-194e-7e597383cad9', '0137_02.jpg', 'Tera_ahblx', 'university rootmate', 'neighbour'),
('d96a955c-b061-7080-194e-7e597383cad9', '0146_01.jpg', 'Tera_ahblx', 'goint outside for dinner', 'friend'),
('d96a955c-b061-7080-194e-7e597383cad9', '0162_01.jpg', 'Tera_ahblx', 'particiate in the wedding', 'neighbour'),
('d96a955c-b061-7080-194e-7e597383cad9', '0202_01.jpg', 'Tera_ahblx', 'just enjoy the time', 'neighbour'),
('d96a955c-b061-7080-194e-7e597383cad9', '0273_01.jpg', 'Tera_ahblx', 'classmate in secondary school', 'neighbour'),
('d96a955c-b061-7080-194e-7e597383cad9', '0292_01.jpg', 'Tera_ahblx', 'goint outside for dinner', 'neighbour'),
('d96a955c-b061-7080-194e-7e597383cad9', '0361_01.jpg', 'Tera_ahblx', 'university rootmate', 'neighbour'),
('d9aa357c-20d1-704c-3877-63edc40201bd', '0001_01.jpg', 'Shala_cmozv', 'walk in the park', 'best friend'),
('d9aa357c-20d1-704c-3877-63edc40201bd', '0013_01.jpg', 'Shala_cmozv', 'have the afternoon tea', 'son'),
('d9aa357c-20d1-704c-3877-63edc40201bd', '0025_01.jpg', 'Shala_cmozv', 'particiate in the wedding', 'best friend'),
('d9aa357c-20d1-704c-3877-63edc40201bd', '0037_02.jpg', 'Shala_cmozv', 'at the birthday party', 'best friend'),
('d9aa357c-20d1-704c-3877-63edc40201bd', '0062_01.jpg', 'Shala_cmozv', 'particiate in the wedding', 'neighbour'),
('d9aa357c-20d1-704c-3877-63edc40201bd', '0072_04.jpg', 'Shala_cmozv', 'watch movie together', 'best friend'),
('d9aa357c-20d1-704c-3877-63edc40201bd', '0101_01.jpg', 'Shala_cmozv', 'particiate in the wedding', 'best friend'),
('d9aa357c-20d1-704c-3877-63edc40201bd', '0113_01.jpg', 'Shala_cmozv', 'university rootmate', 'best friend'),
('d9aa357c-20d1-704c-3877-63edc40201bd', '0158_01.jpg', 'Shala_cmozv', 'university rootmate', 'best friend'),
('d9aa357c-20d1-704c-3877-63edc40201bd', '0170_01.jpg', 'Shala_cmozv', 'walk in the park', 'best friend'),
('d9aa357c-20d1-704c-3877-63edc40201bd', '0183_02.jpg', 'Shala_cmozv', 'visit you at the festival', 'best friend'),
('d9aa357c-20d1-704c-3877-63edc40201bd', '0025_01.jpg', 'Weifeng Sun_obrwz', 'just enjoy the time', 'neighbour'),
('d9aa357c-20d1-704c-3877-63edc40201bd', '0029_01.jpg', 'Weifeng Sun_obrwz', 'meet on the street', 'close friend'),
('d9aa357c-20d1-704c-3877-63edc40201bd', '0054_01.jpg', 'Weifeng Sun_obrwz', 'have the afternoon tea', 'neighbour'),
('d9aa357c-20d1-704c-3877-63edc40201bd', '0058_01.jpg', 'Weifeng Sun_obrwz', 'watch movie together', 'neighbour'),
('d9aa357c-20d1-704c-3877-63edc40201bd', '0062_01.jpg', 'Weifeng Sun_obrwz', 'particiate in the wedding', 'neighbour'),
('d9aa357c-20d1-704c-3877-63edc40201bd', '0070_01.jpg', 'Weifeng Sun_obrwz', 'university rootmate', 'neighbour'),
('d9aa357c-20d1-704c-3877-63edc40201bd', '0125_01.jpg', 'Weifeng Sun_obrwz', 'visit you at the festival', 'neighbour'),
('d9aa357c-20d1-704c-3877-63edc40201bd', '0129_01.jpg', 'Weifeng Sun_obrwz', 'particiate in the wedding', 'neighbour'),
('d9aa357c-20d1-704c-3877-63edc40201bd', '0137_01.jpg', 'Weifeng Sun_obrwz', 'meet on the street', 'nurse'),
('d9aa357c-20d1-704c-3877-63edc40201bd', '0146_01.jpg', 'Weifeng Sun_obrwz', 'particiate in the wedding', 'son'),
('d9aa357c-20d1-704c-3877-63edc40201bd', '0280_01.jpg', 'Weifeng Sun_obrwz', 'meet on the street', 'neighbour'),
]

cursor.executemany("""
                INSERT INTO user_remindee 
               (user_id, image_object_key, person_name, summary, relationship) VALUES (?, ?, ?, ?, ?)
               """, data)

# Commit the changes and close the connection
conn.commit()
conn.close()
