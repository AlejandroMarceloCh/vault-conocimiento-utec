---
curso: BIGDATA
titulo: 13 - Semana 11/Neo4j CheatSheet
slides: 5
fuente: 13 - Semana 11/Neo4j CheatSheet.pdf
---

             Neo4j                                                                        Cypher Cheat Sheet

Cypher is the declarative query language for Neo4j, the world’s leading graph database.

 - Cypher matches patterns of nodes and relationship in the graph, to extract information or modify the data.
 - Cypher has the concept of identifiers which denote named, bound elements and parameters.
 - Cypher can mutate graph data by creating, updating, and removing nodes, relationships, and properties.

You can try cypher snippets live in the Neo4j Console at
http://console.neo4j.org



              Read-Only Query Structure                                         MATCH                              meaning
START me=node:people(name='Andres')                                MATCH n-->m                       A pattern where n has
[MATCH me-[:FRIEND]->friend ]                                                                        outgoing relationships to
WHERE friend.age > 18                                                                                another node, no matter
RETURN me, friend.name                                                                               relationship-type
ORDER BY friend.age asc                                            MATCH n--m                        n has relationship in
SKIP 5 LIMIT 10                                                                                      either direction to m
                                                                   MATCH n-[:KNOWS]->m               The outgoing relationship
                                                                                                     between n and m has to be
                                                                                                     of KNOWS relationship type
           START                         meaning                   MATCH n-[:KNOWS|LOVES]-m          n has KNOWS or LOVES
START n=node(id,[id2,           Load the node with id                                                relationship to m
id3])                           id into n                          MATCH n-[r]->m                    An outgoing relationship
START n=node:indexName          Query the index with an                                              from n to m, and store the
(key="value")                   exact query and put the                                              relationship in r
                                result into n                      MATCH n-[r?]->m                   The relationship is
                                                                                                     optional
                                Use node_auto_index for
                                the auto-index                     MATCH n-[*1..5]->m                A multi step relationship
                                                                                                     between between n and m,
                                                                                                     one and five steps away
START n=node:indexName          Query the index using a
("lucene query")                full Lucene query and              MATCH n-[*]->m                    A pattern where n has a
                                put the result in n                                                  relationship to m unbound
                                                                                                     number of steps away
START n=node(*)                 Load all nodes
                                                                   MATCH n-[?:KNOWS*..5]->m          An optional relationship
START m=node(1),                Multiple start points                                                between n and m that is of
n=node(2)                                                                                            KNOWS relationship type,
                                                                                                     and between one and five
                                                                                                     steps long.
                                                                   MATCH n-->m<--o                   A pattern with n having an
           RETURN                        meaning                                                     outgoing relationship to
RETURN *                        Return all named nodes,                                              m, and m having incoming
                                relationships and iden-                                              relationship from o
                                tifiers
                                                                   MATCH p=n-->m<--o                 Store the path going from
RETURN expr AS alias            Set result column name                                               n to o over m into the
                                as alias                                                             path identifier p
RETURN distinct                 Return unique values               MATCH p = shortestPath(           Find the shortest path
expr                            for expr                           n-[:KNOWS*3]->m )                 between n and m of type
                                                                                                     KNOWS of at most length 3




                                                                                                                                 neo4j.org
                                                                                                                        neotechnology.com
                                                                                                                © 2012 Neo Technology Inc.
 Cypher Cheat Sheet                                                                                      2




         Read-Write-Return Query Structure                      SET                       meaning
START emil=node:people(name='Emil')                  SET n.prop = value         Updates or creates the
MATCH emil-[:MARRIED_TO]-madde                                                  property prop with the given
CREATE/CREATE UNIQUE                                                            value
emil-[:DAD]->(noomi {name:"Noomi"})<-[:MOM]-madde    SET n = {map}              Updates the properties with
DELETE emil.spare_time                                                          the given map
SET emil.happy=true                                                             parameter
RETURN noomi
                                                     SET n.prop = null          Deletes the property prop



         CREATE                   meaning                   Predicates                    meaning
CREATE (n {                Creates the node with     NOT pred1 AND/OR pred2     Boolean operators for
name :"Name" })            the given properties                                 predicates
CREATE n = {map}           Create node from map      ALL(x in coll: pred)       TRUE if pred is TRUE for all
                           parameter                                            values in
                                                                                coll
CREATE n = {manyMaps}      Create many nodes from
                           parameter with            ANY(x in coll : pred)      TRUE if pred is TRUE for at
                           coll of maps                                         least one value in coll
CREATE n-[:KNOWS]->m       Creates the               NONE(x in coll : pred)     TRUE if pred returns FALSE
                           relationship with the                                for all values in
                           given type and dir                                   coll
CREATE n-[:LOVES           Creates the               SINGLE(x in coll : pred)   TRUE if pred returns TRUE
{since: 2007}] ->m         relationship with the                                for a single value in coll
                           given type, dir, and      identifier IS NULL         TRUE if identifier is <NULL>
                           properties
                                                     n.prop? = value            TRUE if n.prop = value or n
                                                                                is NULL or n.prop does not
                                                                                exist
         DELETE                   meaning
                                                     n.prop! = value            TRUE if n.prop = value,
DELETE n, DELETE rel       Deletes the node,                                    FALSE if n is NULL or n.prop
                           relationship                                         does not exist
DELETE n.prop              Removes the property      n =~ /regexp/              Regular expression
                                                     e1 <> e2                   Comparison operators
                                                     e1 < e2
     CREATE UNIQUE                meaning            e1 = e2
CREATE UNIQUE              Tries to match the        has(n.prop)                Checks if property exists
n-[:KNOWS]->m              pattern. Creates the
                                                     n-[:TYPE]->m               Filter on existence of
                           missing pieces if the
                                                                                relationship
                           match fails
                                                     expr IN coll               Checks for existence of expr
CREATE UNIQUE              Tries to match a node
                                                                                in coll
n-[:KNOWS]->(m             with the property name
{name:"Name"})             set to "Name". Creates
                           the node and sets the
                           property if it can’t be
                           found.
CREATE UNIQUE              Tries to find the
n-[:LOVES {since: 2007}]   relationship with the
->m                        given type, direction,
                           and attributes.
                           Creates it if not
                           found.




                                                                                                         neo4j.org
                                                                                                neotechnology.com
                                                                                        © 2012 Neo Technology Inc.
 Cypher Cheat Sheet                                                                                      3



      Expressions                    meaning               Path Functions                meaning
       a-zA-Z0-9_          Allowed identifier         NODES(path)              Returns the nodes in path
           or              (or quoted)                RELS(path)               Returns the relationships in
      'some na-me'
                                                                               path
n + / - * % m              Arithmetic operators       LENGTH(path)             Returns the length of path
                           "+" also works on
                           strings and collections
n.prop, n.prop?            Property on node,
                           property on node, or
                           NULL if missing
                                                         Aggregate Functions
                                                      COUNT([distinct] expr)             meaning
                                                                               Returns the number of non-
                                                                               NULL values in expr
[42,"Hello",'World',{p}]   A collection
                                                      COUNT(*)                 Returns the number of values
{param}                    Parameter value, passed                             aggregated over
                           into the query execution
                           as map                     SUM(expr)                Returns the sum of all
                           { param : "value",... }                             values in expr
                                                                               Throws exception for
a-->()<--b                 A path-pattern                                      non-numeric values
                                                      AVG(expr)                Returns the average of all
                                                                               values in expr
                                                      MAX(expr)                Returns the largest value in
           Functions                 meaning                                   expr
HEAD(coll)                   First element of         MIN(expr)                Returns the smallest values
                             coll                                              in expr
TAIL(coll)                   coll except first        COLLECT(expr)            Returns an coll containing
                             element                                           all values in expr
LAST(coll)                   Last element of          FILTER( x in coll :      Returns a all the elements
                             coll                     predicate )              in coll that match the given
TYPE(rel)                    Relationship type of                              predicate
                             rel                      EXTRACT( x in coll :     Applies the
ID(node)                     Id of node or            expr)                    expr once for every element
ID(relationship)             relationship                                      in coll

COALESCE(expr,default)       Returns default if
                             expr is NULL
                             otherwise expr

RANGE(start,end[,step])      Creates a range from
                             start to end
                             (inclusive) with a
                             optional step
ABS(v)                       Math functions
ROUND(v)
SQRT(v)
SIGN(v)




                                                                                                        neo4j.org
                                                                                               neotechnology.com
                                                                                       © 2012 Neo Technology Inc.
 Cypher Cheat Sheet                                                                                                            4



                         FOREACH                                                              Useful Snippets
FOREACH is used to execute a mutating operation for each         START n=node(...)                  Not already connected to
element of a collection, e.g. creating a node for each ele-      MATCH n-->m-->o
                                                                 WHERE not ( n-->o )                This returns nodes that m is
ment
                                                                 RETURN o                           connected to, that n is not
using the element as an attribute value.                                                            already connected to.

START user=node:users("name:A*"),
promotion=node(...)
                                                                 START n=node(...)                  Find cycles
MATCH user-[:FRIEND]-friend-[:FRIEND]-foaf
                                                                 MATCH path = n-[*]-n
WITH user, collect(distinct foaf) as new_friends
                                                                 RETURN n, length(path)             This returns nodes that m is
                                                                                                    connected to, that n is not
                                                                                                    already connected to.
                                                                 START n=node(...)                  Group count relationship
                            WITH                                 MATCH n-[r]-m                      types
                                                                 RETURN type(r), count(*)
WITH syntax is similar to RETURN. It separates query parts
                                                                                                    Returns a count of each of
explicitly, allowing you to declare which identifiers to carry                                      the relationship-types.
over to the next part. This can be used to limit the visible
                                                                 START n=node(...)                  Delete node with
identifiers but mostly for creating aggregate values that can
                                                                 MATCH n-[r?]-()                    relationships
be used in the next query part either for filtering              DELETE n,r
(implementing HAVING) or for the creation of new structures                                         Finds the node and all
in the graph.                                                                                       relationships (if any) and
                                                                                                    deletes node and
WITH also creates a boundary between reading and                                                    relationships.
updating query parts so that they don’t interfere.               START n = node(1), m =             String concat on expressions
                                                                 node(2) RETURN n.name
START user=node:users("name:A*")                                 +" and "+ m.name
MATCH user-[:FRIEND]-friend
WITH user, count(friend) as friends
WHERE friends > 10                                                                             Useful Links
RETURN user
                                                                 Cypher Screencast
START user=node:users("name:A*")                                 http://bit.ly/cypher-stanley
MATCH user-[:FRIEND]-friend
WITH user, count(friend) as friends                              Cypher Reference Manual
SET user.numberOfFriends = friends                               http://bit.ly/cypher-reference

                                                                 Cypher Presentation
                                                                 http://bit.ly/cypher-slide
                       Transactions

The Neo4j-Shell supports commands to begin transactions,
which allows you issue multiple commands and then only
commit them when you’re satisfied and rollback if you ran into
an issue or don’t want your changes to happen.

neo4j-sh (0)$ begin
==> Transaction started
neo4j-sh (0)$ rollback
==> Transaction rolled back
neo4j-sh (0)$ commit
==> Transaction committed




                                                                                                                               neo4j.org
                                                                                                                      neotechnology.com
                                                                                                              © 2012 Neo Technology Inc.
Cypher Cheat Sheet                     5




                                      neo4j.org
                             neotechnology.com
                     © 2012 Neo Technology Inc.
