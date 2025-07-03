#EXAMPLE
#QUERY = 'db.names.find({name: "John Doe"})'

FIRST_QUERY = 'db.users.insertOne({ name: "Cory Silverman", email: "cory.silverman@test.com" })'

SECOND_QUERY = 'db.movies.find({ directors: "Christopher Nolan" })'

THIRD_QUERY = 'db.movies.find({ genres: "Action" }).sort({ year: -1 })'

FOURTH_QUERY = 'db.movies.find({ "imdb.rating": { $gt: 8 }}, { _id: 0, title: 1, imdb: 1})'

FIFTH_QUERY = 'db.movies.find({ cast: { $all: ["Tom Hanks", "Tim Allen"] }})'

SIXTH_QUERY = 'db.movies.find({ $and: [{ cast: { $all: ["Tom Hanks", "Tim Allen"] } }, { cast: { $size: 2 } }]})'

SEVENTH_QUERY = 'db.movies.find({ $and: [{ genres: "Comedy" }, { directors: "Steven Spielberg" }]})'

EIGTH_QUERY = 'db.movies.updateOne({ _id: ObjectId("573a139bf29313caabcf3d23") }, { $set: { available_on: "Sflix" } })'

NINETH_QUERY = 'db.movies.updateOne({ _id: ObjectId("573a139bf29313caabcf3d23") }, { $inc: { metacritic: 1 } })'

TENTH_QUERY = 'db.movies.updateMany({ year: 1997 }, { $push: { genres: "Gen Z" } })'

ELEVENTH_QUERY = 'db.movies.updateMany({ "imdb.rating": { $lt: 5 } }, { $inc: { "imdb.rating": 1 } })'

TWELVETH_QUERY = 'db.comments.deleteOne({ _id: ObjectId("5a9427648b0beebeb69589f2") })'

THIRTEENTH_QUERY = 'db.comments.deleteMany({ movie_id: ObjectId("573a139bf29313caabcf3d23") })'

FOURTEENTH_QUERY = 'db.movies.deleteMany({ genres: { $size: 0 } })'

FIVETEENTH_QUERY = 'db.movies.aggregate([{ $group: { _id: "$year", count: { $sum: 1 } } }, { $sort: { _id: 1 } }])'

SIXTEENTH_QUERY = 'db.movies.aggregate([{ $group: { _id: "$directors", averageRating: { $avg: "$imdb.rating" } } }, {$sort: { averageRating: -1 } }])'