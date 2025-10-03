db
test
use University
switched to db University
db.Student.insertOne()
MongoshInvalidInputError: [COMMON-10001] Missing required argument at position 0 (Collection.insertOne)
db.Student.insertOne({
  student_id:1,
  name:"Rahul",
  age: 21,
  city: "Mumbai",
  course: "AI",
  marks: 85
})
{
  acknowledged: true,
  insertedId: ObjectId('68dfa44a3d4cb9740786431b')
}
db.Student.insertMany([
  {student_id: 2, name: "Priya", age: 22, city: "Delhi", course: "ML", marks: 90},
  {student_id: 3, name: "Arjun", age: 20, city: "Bengaluru", course: "Data Scienec", marks: 78},
  {student_id: 4, name: "Neha", age: 23, city: "Hyderabad", course: "AI", marks: 88},
  {student_id: 5, name: "Vikram", age: 21, city: "Chennai", course: "ML", marks: 95}
])
{
  acknowledged: true,
  insertedIds: {
    '0': ObjectId('68dfa7053d4cb9740786431c'),
    '1': ObjectId('68dfa7053d4cb9740786431d'),
    '2': ObjectId('68dfa7053d4cb9740786431e'),
    '3': ObjectId('68dfa7053d4cb9740786431f')
  }
}
db.Students.find()
db.Student.find()
{
  _id: ObjectId('68dfa44a3d4cb9740786431b'),
  student_id: 1,
  name: 'Rahul',
  age: 21,
  city: 'Mumbai',
  course: 'AI',
  marks: 85
}
{
  _id: ObjectId('68dfa7053d4cb9740786431c'),
  student_id: 2,
  name: 'Priya',
  age: 22,
  city: 'Delhi',
  course: 'ML',
  marks: 90
}
{
  _id: ObjectId('68dfa7053d4cb9740786431d'),
  student_id: 3,
  name: 'Arjun',
  age: 20,
  city: 'Bengaluru',
  course: 'Data Scienec',
  marks: 78
}
{
  _id: ObjectId('68dfa7053d4cb9740786431e'),
  student_id: 4,
  name: 'Neha',
  age: 23,
  city: 'Hyderabad',
  course: 'AI',
  marks: 88
}
{
  _id: ObjectId('68dfa7053d4cb9740786431f'),
  student_id: 5,
  name: 'Vikram',
  age: 21,
  city: 'Chennai',
  course: 'ML',
  marks: 95
}
db.Student.findOne({name:"Rahul"})
{
  _id: ObjectId('68dfa44a3d4cb9740786431b'),
  student_id: 1,
  name: 'Rahul',
  age: 21,
  city: 'Mumbai',
  course: 'AI',
  marks: 85
}
db.Student.find({marks: {$gt: 85}})
{
  _id: ObjectId('68dfa7053d4cb9740786431c'),
  student_id: 2,
  name: 'Priya',
  age: 22,
  city: 'Delhi',
  course: 'ML',
  marks: 90
}
{
  _id: ObjectId('68dfa7053d4cb9740786431e'),
  student_id: 4,
  name: 'Neha',
  age: 23,
  city: 'Hyderabad',
  course: 'AI',
  marks: 88
}
{
  _id: ObjectId('68dfa7053d4cb9740786431f'),
  student_id: 5,
  name: 'Vikram',
  age: 21,
  city: 'Chennai',
  course: 'ML',
  marks: 95
}
db.Student.find({},{name: 1, course:1, _id:0})
{
  name: 'Rahul',
  course: 'AI'
}
{
  name: 'Priya',
  course: 'ML'
}
{
  name: 'Arjun',
  course: 'Data Scienec'
}
{
  name: 'Neha',
  course: 'AI'
}
{
  name: 'Vikram',
  course: 'ML'
}
db.Student.updateOne(
  {name: "Neha"},
  {$set: {marks: 92, course: "Advanced AI"}}
)
{
  acknowledged: true,
  insertedId: null,
  matchedCount: 1,
  modifiedCount: 1,
  upsertedCount: 0
}
db.Student.updateMany(
  {course: "AI"},
  {$set: {grade: "A"}}
)
{
  acknowledged: true,
  insertedId: null,
  matchedCount: 1,
  modifiedCount: 1,
  upsertedCount: 0
}
db.Student.deleteOne({name: "Arjun"})
{
  acknowledged: true,
  deletedCount: 1
}
db.Student.deleteMany({marks: {$lt:80}})
