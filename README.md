BFS (Breadth-First Search) (1,2,3)– Undirected Graph

    ALGORITHM BFS(Graph, N, E, Start)

    BEGIN
        Create an empty adjacency list Graph

        FOR each edge from 1 to E DO
            Read vertices U and V
            Add V to Graph[U]
            Add U to Graph[V]
        END FOR

        Create an empty queue Q
        Create an empty set Visited
    
        Mark Start as visited
        Insert Start into Q

        WHILE Q is not empty DO
            Node = Remove the front element from Q
            Print Node

            FOR each Neighbor in Graph[Node] DO
                IF Neighbor is not in Visited THEN
                    Mark Neighbor as visited
                    Insert Neighbor into Q
                END IF
            END FOR
        END WHILE
    END

###BFS (Breadth-First Search) 4 – Directed Graph

    ALGORITHM BFS(Graph, N, E, Start)

    BEGIN
        Create an empty adjacency list Graph

        FOR each edge from 1 to E DO
            Read vertices U and V
            Add V to Graph[U]
        END FOR

        Create an empty queue Q
        Create an empty set Visited

        Mark Start as visited
        Insert Start into Q

        WHILE Q is not empty DO
            Node = Remove the front element from Q
            Print Node

            FOR each Neighbor in Graph[Node] DO
                IF Neighbor is not in Visited THEN
                    Mark Neighbor as visited
                    Insert Neighbor into Q
                END IF
            END FOR
        END WHILE
    END


DFS (Depth-First Search) – Directed and Undirected Graphs

    ALGORITHM DFS(Graph, N, E)

    BEGIN
        Read GraphType (directed or undirected)
        Read number of vertices N
        Read number of edges E

        Create an empty adjacency list Graph

            FOR each edge from 1 to E DO
            Read vertices U and V
            Add V to Graph[U]

            IF GraphType = undirected THEN
                Add U to Graph[V]
            END IF
        END FOR

        Read starting vertex Start
        Create an empty set Visited
        Create an empty list Result

            PROCEDURE Explore(Node)
            Mark Node as visited
            Add Node to Result

            FOR each Neighbor in Graph[Node] DO
                IF Neighbor is not in Visited THEN
                    Explore(Neighbor)
                END IF
            END FOR
        END PROCEDURE

        IF Start is a valid vertex THEN
            Call Explore(Start)
            Print Result
        ELSE
            Print "Invalid starting vertex"
        END IF
    END

Time Complexity: O(V + E)

Space Complexity: O(V + E)
