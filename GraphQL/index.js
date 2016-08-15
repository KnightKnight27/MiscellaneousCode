// Javascript module imports
var graphql = require('graphql');
var graphqlHTTP = require('express-graphql');
var express = require('express');

// Apparently you can import data in the same way as you can import modules (but
// are there security risks here, i.e. can importing data in this way lead to execution
// of arbitrary code?
var data = require('./data.json');

// Define a 'user type' from the GraphQL types and javascript object
// syntax
var userType = new graphql.GraphQLObjectType({
    name: 'User',
    fields: {
        id: {type: graphql.GraphQLString},
        name: {type: graphql.GraphQLString},
}
});

// Now define a schema for the data we are accessing. This defines the queries that
// we can make against this data (I think), and the data returned for each query.
var schema = new graphql.GraphQLSchema({
    query: new graphql.GraphQLObjectType({
        name: 'Query',
        fields: {
            user: {
                type: userType,
                // 'args' here defines the arguments that the 'user' query will accept
                args: {
                    id: {type: graphql.GraphQLString}
                },
                // The 'resolve' function now describes how the query is handled.
                resolve: function (_, args) {
                    return data[args.id]; // This does a map look-up. Not sure how this is implemented in Javascript.
                }
              }
            }
        })
});


const port = 3010;

express()
    .use('/graphql', graphqlHTTP({schema: schema, pretty: true}))
    .listen(port);


console.log('GraphQL server running on http://localhost:' + port + '/graphql');
