import model
from model import User, Burrito, Question

# remember that SQL Datatypes are INTEGERS!! NEED TO CHANGE TO DECIMAL!

# Category: Spicy
# "If I were a pokemon, I would be: " -pikachu -squirtle - charmander

#psuedo code .2
# opinion needs to get clicked via checkbox
# when opinion picked, needs to relate to -1 to 1
# insert opinion into db
# user needs to choose a weight, which spans 0-1 
# insert weight into database
# opinion * weight = score
# insert score into a Category in db
# Category needs to be displayed in bar graph


# opinion = {'pikachu': 1,
# 		   'squirtle': 1,
# 		   'charmander': 1}


user_info = [1, 1]
opinion = [1]
# need to figure the decimal thing in database
# weight = [2, 1, 0]

def question():
	#need to pull a question from the database
	pass

#need to call the db to insert my hard coded data

#zip the row with the dict
def insert_score(session):
	#first get row
	row = []
	row = session.query(model.Question).get(1)
	#define dict columns
	print "row type",type(row)
	print row.text
	# fields = ['id', 'q_id', 'text','answer','weight',
	# 		  'score','category','user_id','burrito_id']	
	# new_object = dict(zip(fields,row))
	# print "Type yo",type(new_object)	
	# print new_object	  

	#update row with user info
	row.user_id =  user_info[0]
	row.answer = user_info[1]
	session.commit()
	print row.text, row.answer, row.user_id


	# score = opinion * weight 
	# print 'TYPE', type(score)
	# update_object = Question()
	# session.commit()

def main(session):
	# You'll call each of the load_* functions with the session as an argument
  insert_score(session)


if __name__ == "__main__":
	s= model.connect()
	main(s)	


