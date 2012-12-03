from random import *
import time
class Person(object):
	"""
	Person class
		aspects of personality based on Myers Briggs Personality types
		mood (int) -50 to 50
		name (string)

	energy => Natural energy (extraverted to introverted)
	perception => (sensing to intuitive)
	judgement => (thinking to feeling)
	action => (judging to perceiving)

	Boolean values:
		true / false => extraverted / introverted; etc
	"""
	__slots__ = ("name", "mood", "energy", "perception", "judgement", "action")

	def __init__(self, name, m=bool(getrandbits(1)), e=bool(getrandbits(1)), p=bool(getrandbits(1)), j=bool(getrandbits(1)), a=bool(getrandbits(1))):
		"""
		Initializes a person with set personality and neutral mood
		"""
		self.name = name
		self.mood = m
		self.energy = e
		self.perception = p
		self.judgement = j
		self.action = a

	def __str__(self):
		"""
		Returns character mood and personality type
		"""
		ptype = ""
		if self.energy:
			ptype += "E"
		else:
			ptype += "I"
		if self.perception:
			ptype += "S"
		else:
			ptype += "I"
		if self.judgement:
			ptype += "T"
		else:
			ptype += "F"
		if self.action:
			ptype += "J"
		else:
			ptype += "P"


		return(self.name + ":\n" + "\tMood:\t" + str(self.mood) + "\n\tType:\t" + ptype)


class Relationship(object):
	"""
	Relationship class
		p1 (Person) Person 1
		p2 (Person) Person 2
		commitment (int) in the short term, the decision to remain with another, and in the long term, the shared achievements and plans made with that other
		intimacy (int) feelings of attachment, closeness, connectedness, and bondedness
		passion (int) encompasses drives connected to both limerence and sexual attraction

	Based on Robert Sternberg's "Triangular Theory of Love"
	"""

	__slots__ = ("p1", "p2", "commitment", "intimacy", "passion")

	def __init__(self, adam, steve):
		"""
		Initializes a relationship with two people, setting zero values to begin
		"""
		self.p1 = adam
		self.p2 = steve
		self.commitment = 0
		self.intimacy = 0
		self.passion = 0

	def __str__(self):
		"""
		Returns passion, commitment, and intimacy values in addition to an "rtype" or "Relationship Type"
		"""
		rtype = ""
		INTIMACY_THRESHOLD = 5
		PASSION_THRESHOLD = 5
		COMMITMENT_THRESHOLD = 5
		if self.intimacy >= INTIMACY_THRESHOLD and self.passion <= INTIMACY_THRESHOLD and self.commitment <= INTIMACY_THRESHOLD:
			rtype = "Friendship"
		elif self.intimacy <= INTIMACY_THRESHOLD and self.passion >= PASSION_THRESHOLD and self.commitment <= INTIMACY_THRESHOLD:
			rtype = "Infatuated Love"
		elif self.intimacy <= INTIMACY_THRESHOLD and self.passion <= INTIMACY_THRESHOLD and self.commitment >= COMMITMENT_THRESHOLD:
			rtype = "Empty Love"
		elif self.intimacy >= INTIMACY_THRESHOLD and self.passion >= PASSION_THRESHOLD and self.commitment <= INTIMACY_THRESHOLD:
			rtype = "Romantic Love"
		elif self.intimacy >= INTIMACY_THRESHOLD and self.passion <= INTIMACY_THRESHOLD and self.commitment >= COMMITMENT_THRESHOLD:
			rtype = "Companionate Love"
		elif self.intimacy >= INTIMACY_THRESHOLD and self.passion >= PASSION_THRESHOLD and self.commitment >= COMMITMENT_THRESHOLD:
			rtype = "Fatuous Love"
		elif self.intimacy >= INTIMACY_THRESHOLD and self.passion >= PASSION_THRESHOLD and self.commitment >= COMMITMENT_THRESHOLD:
			rtype = "Consummate Love"
		else:
			rtype = "No Standing Relationship"

		return "Relationship between " + self.p1.name + " and " + self.p2.name + ":\n\tType:\t\t" + rtype + "\n\tCommitment:\t" + str(self.commitment) + "\n\tIntimacy: \t" + str(self.intimacy) + "\n\tPassion: \t" + str(self.passion)

	def progress(self):
		"""
		Representing day to day life
			Calculates random mood changes in both people
			Advances intimacy, passion, and commitment based on Myers Briggs compatibility combinations
		"""
		self.p1.mood += randint(-2,2)
		self.p2.mood += randint(-2,2)
		self.intimacy = randint(-2,3) + (self.p1.energy == self.p2.energy if 2 else 0) + (self.p1.mood // 5) + (self.p2.mood // 5)
		self.passion = randint(-1,3) + (self.p1.judgement == self.p2.judgement if 2 else 0) + (self.p1.mood // 5) + (self.p2.mood // 5)
		self.commitment = randint(-2,3) + (self.p1.energy == self.p2.energy if 1 else 0) + (self.p1.mood // 5) + (self.p2.mood // 5)

def main():
	"""
	Runs "life" for a set period of iterations
	"""
	seed()
	people = list()
	people.append(Person("Charles", 0, bool(getrandbits(1)), bool(getrandbits(1)), bool(getrandbits(1)), bool(getrandbits(1))))
	people.append(Person("Beth", 0, bool(getrandbits(1)), bool(getrandbits(1)), bool(getrandbits(1)), bool(getrandbits(1))))
	people.append(Person("Kate", 0, bool(getrandbits(1)), bool(getrandbits(1)), bool(getrandbits(1)), bool(getrandbits(1))))
	people.append(Person("Ian", 0, bool(getrandbits(1)), bool(getrandbits(1)), bool(getrandbits(1)), bool(getrandbits(1))))

	connections = list()
	for i in people:
		for j in people:
			if i != j:
				connections.append(Relationship(i,j))

	#connections.append(Relationship(Person("Charles", 0, bool(getrandbits(1)), bool(getrandbits(1)), bool(getrandbits(1)), bool(getrandbits(1))), Person("Beth", 0, bool(getrandbits(1)), bool(getrandbits(1)), bool(getrandbits(1)), bool(getrandbits(1)))))
	for r in range(0,15):
		for c in connections:
			print("Mingling...")
			print(c.p1)
			print(c.p2)
			c.progress()
			print(c)
			#time.sleep(2)

main()