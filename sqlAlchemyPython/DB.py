"""
Following program creates the Diners DataBase with using of SQLAlchemy
Two related tables Canteen and Provider
query: return the canteens that are open from 16.15-18.00

"""
import sqlite3
import sqlalchemy as sql
from sqlalchemy.orm import sessionmaker
import datetime as dt
from sqlalchemy.ext.declarative import declarative_base



Base = declarative_base()
engine = sql.create_engine('sqlite:///dinners.db', echo=True)

#create table Canteen
class Canteen(Base):
	     __tablename__ = 'canteens'

	     id = sql.Column(sql.Integer, primary_key=True)
	     ProviderID = sql.Column(sql.Integer, sql.ForeignKey('providers.id'))
	     Name = sql.Column(sql.String)
	     Location = sql.Column(sql.String)
	     time_open = sql.Column(sql.types.Time)
	     time_closed = sql.Column(sql.types.Time)

	     def __repr__(self):
	        return "<Canteen(name='%s', location='%s', time_open='%s', time_closed='%s )>" % (
	                            self.name, self.location, self.time_open, self.time_closed)
#Create table provider
class Provider(Base):
	__tablename__ = 'providers'
	id = sql.Column(sql.Integer, primary_key=True)
	ProviderName = sql.Column(sql.String)
	
	def __repr__(self):
		return "<Provider(name='%s')>" % self.ProviderName

# add values
canteens = [Canteen(id=1, Name='ESS building canteen', ProviderID=1, Location='Akadeemia tee 3 SOC-building', time_open=dt.time(8,30), time_closed=dt.time(18,30)),
		  Canteen(id=2, Name='Library canteen', ProviderID=1, Location='Akadeemoia tee 1/Ehitajate tee 7', time_open=dt.time(8,30), time_closed=dt.time(19)),
		  Canteen(id=3, Name='Main building Deli cafe', ProviderID=2, Location='Ehitajate tee 5 U01 building', time_open=dt.time(9), time_closed=dt.time(16,30)),
		  Canteen(id=4, Name='Main building Daily lunch restaurant', ProviderID=2, Location='Ehitajate tee 5 U01 building', time_open=dt.time(9), time_closed=dt.time(16)),
		  Canteen(id=5, Name='U06 building canteen', ProviderID=1, Location='U06 building', time_open=dt.time(9), time_closed=dt.time(16)),
		  Canteen(id=6, Name='Natural science buiding canteen',ProviderID=2, Location='Akadeemia tee 15 SCI building', time_open=dt.time(9), time_closed=dt.time(16)),
		  Canteen(id=7, Name='ICT building canteen', ProviderID=2, Location='Raja 15/Mäepealse 1', time_open=dt.time(9), time_closed=dt.time(16)),
		  Canteen(id=8, Name='Sports building canteen', ProviderID=3, Location='Männiliiva 7 S01 building', time_open=dt.time(11), time_closed=dt.time(20))
		  ]
providers = [Provider(id=1, ProviderName="Rahva Toit"),
			Provider(id=2, ProviderName="Baltic Restaurants Estonia AS"),
			Provider(id=3, ProviderName="TTU Sport"),
			Provider(id=4, ProviderName="BitStop Kohvik OU")
			]
engine = sql.create_engine('sqlite:///Dinners.db', echo=True)

Base.metadata.create_all(engine)


if __name__ == "__main__":
	Session = sessionmaker(bind=engine)
	session = Session()		
	session.add_all(canteens)
	session.add_all(providers)



	iTCollege = Canteen(Name='bitStop KOHVIK', ProviderID=4, Location="Raja 4C", time_open=dt.time(9,30), time_closed=dt.time(16));
	session.add(iTCollege)
	session.commit()
	
	# open from  16.15-18.00
	for row in session.query(Canteen).filter(Canteen.time_open <= dt.time(16,15)).filter(Canteen.time_closed >= dt.time(18)).all():
		
		print(row.Name)

	print()
	print()

	#canteens which are serviced by Rahva Toit
	for row in session.query(Canteen).filter(Provider.ProviderName=="Rahva Toit").all():
		print(row.Name)
		

	
	