//https://onecompiler.com/mongodb
db.employees.insertMany([
  {_id: 1, name: 'Clark', dept: 'Sales' },
  {_id: 2, name: 'Dave', dept: 'Accounting' },
  {_id: 3, name: 'Ava', dept: 'Sales' }
]);
db.tired.insertOne({_id:67,nome : 'Diego', state : 'tired',time : 'Now'})
db.tired.find()
db.tired.deleteOne()
db.employees.find({dept: 'Sales'});
db.createCollection("67")
//show collections;
db.getCollection()