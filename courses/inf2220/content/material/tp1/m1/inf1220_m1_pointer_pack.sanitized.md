# INF1220 — Module 1 Pointer Pack (Sanitized Extracts)

- Generated: 2026-01-14

- Purpose: Minimal sanitized authority extracts for deterministic M1 learning-material generation.

- Rule: Use this pack as the primary authority surface; raw Hugo/HTML sources are audit-only.


---

## Index (topics → pack refs)

### m1-07

- Prerequisites & expected prior knowledge → #pack-m1-07-prerequisites
- What an algorithm is (definition, properties, examples) → #pack-m1-07-what-is-an-algorithm
- What pseudocode is (purpose, conventions, readability) → #pack-m1-07-what-is-pseudocode
- Variables and values (assignment, initialization, basic types) → #pack-m1-07-variables-and-values
- Boolean logic (true/false, AND/OR/NOT, precedence, parentheses) → #pack-m1-07-boolean-logic
- Math recall: propositions & truth tables (formal basis for AND/OR/NOT) → #pack-math-logic
- Math recall: implication / equivalence as “spec language” for conditions → #pack-m1-07-boolean-logic
- Conditionals in pseudocode (IF / THEN / ELSE / END IF) → #pack-m1-07-boolean-logic
- Math recall: binary relations (equivalence, order) as the model for comparisons/tests → #pack-math-logic
- Programmer notation (symbolic operators: &&, ||, !) → #pack-m1-07-programmer-notation
- Loops (iteration, counters, termination conditions) → #pack-m1-07-boolean-logic
- Arrays (indexing concept, 0-based vs 1-based, access by index) → #pack-m1-07-array
- Accumulator pattern (sum/average over an array) → #pack-m1-07-array
- Flowchart ↔ pseudocode mapping (average example) → #pack-m1-07-average-example
- Translating pseudocode to real code (Java example) → #pack-m1-07-average-example

### m1-08

- Designing an algorithm (problem analysis: inputs, outputs, processing) → #pack-m1-08-design
- Math recall: sets as input/output domains (∅, membership, cardinality) → #pack-math-sets
- Algorithm syntax (structuring pseudocode) → #pack-m1-08-syntax
- Inputs, variables, and outputs (algorithm interface) → #pack-m1-08-io
- Math recall: cartesian product (A×B) for paired inputs/outputs (tuples) → #pack-m1-08-io
- Operations (arithmetic, comparison, assignment) → #pack-m1-08-operations
- Math recall: order relations (≤, <, ≥, >) and their properties (used in bounds/tests) → #pack-math-relations
- Math recall: number sets (ℕ, ℤ, ℚ, ℝ) as “legal value spaces” for variables → #pack-math-sets
- Math recall: Euclidean division / remainder (mod) for divisibility tests (TP1-style logic) → #pack-math-numbers
- Worked example: count vowels in a typed word → #pack-m1-08-example-vowels

### m1-09

- Jump (goto) and labels (conceptual; generally avoided in modern style) → #pack-m1-09-jump
- Branching as a control structure (conditional jumps / IF logic) → #pack-m1-09-jump
- Loop as a control structure (repetition patterns) → #pack-m1-09-loop
- Composition (combining control structures) → #pack-m1-09-composition
- Ending an algorithm (termination / stop conditions) → #pack-m1-09-ending
- Executing pseudocode (step-by-step tracing) → #pack-m1-09-tracing

### m1-10

- Heuristic algorithm example: nearest-neighbor approach (pseudocode) → #pack-m1-10-tsp-nearest-neighbor
- Distance table (km) as input data → #pack-m1-10-distance-table
- Current-state tracking during iterative construction → #pack-m1-10-tsp-nearest-neighbor

### m1-11

- Big-O notation (what it expresses; growth vs input size) → #pack-m1-11-big-o
- Math recall: sequences/series + Σ intuition (counting steps → growth rates) → #pack-math-series
- Examples: O(n) algorithms (linear time) → #pack-m1-11-examples
- Examples: O(n^2) algorithms (quadratic time) → #pack-m1-11-examples
- Search in a sorted array (complexity framing) → #pack-m1-11-binary-search
- Sorting (complexity framing) → #pack-m1-11-sorting
- Hash table (expected-time intuition) → #pack-m1-11-hash-table
- Same problem, different solutions: O(n^2) vs O(n) → #pack-m1-11-examples
- Trees in computer science (high-level complexity intuition) → #pack-m1-11-trees
- Amortized analysis (high-level idea) → #pack-m1-11-amortized

### m1-12

- Formal-looking but ambiguous pseudocode → #pack-m1-12-common-errors
- Loop condition that forces immediate termination (always-true stop condition) → #pack-m1-12-common-errors
- Non-terminating loops (infinite loops) → #pack-m1-12-common-errors
- Using undefined variables/functions (meaning must be guessed) → #pack-m1-12-common-errors
- Types/syntax look OK, but values/logic are wrong (semantic errors) → #pack-m1-12-common-errors
- Lack of rigor (careless reasoning / missing checks) → #pack-m1-12-common-errors

### m1-13

- Indentation → #pack-m1-13-style-guide
- Terminology (inputs/outputs/variables/functions) → #pack-m1-13-style-guide
- Comments (how/when to annotate pseudocode) → #pack-m1-13-style-guide
- Typography (naming, symbols, readability) → #pack-m1-13-style-guide
- Guide to presenting pseudocode (style/clarity) → #pack-m1-13-style-guide

### m1-14

- Unique answers? (expect multiple valid solutions) → #pack-m1-14-meta
- Software tools (you can use any, but pseudocode is tool-independent) → #pack-m1-14-meta
- Exercise 1: Sum of an array → #pack-m1-14-ex01
- Exercise 2: Searching for an integer → #pack-m1-14-ex02
- Exercise 3: Sum of multiples of 3 or 5 → #pack-m1-14-ex03
- Exercise 4: Largest prime divisor → #pack-m1-14-ex04
- Exercise 5: Tens digit → #pack-m1-14-ex05
- Exercise 6: Error in pseudocode → #pack-m1-14-ex06
- Exercise 7: Roots of a quadratic polynomial → #pack-m1-14-ex07
- Exercise 8: Executing the roots algorithm → #pack-m1-14-ex08
- Exercise 9: Base conversion → #pack-m1-14-ex09
- Exercise 10: Test parity in base 2 → #pack-m1-14-ex10
- Exercise 11: Compute factorial → #pack-m1-14-ex11
- Exercise 12: Reverse an array → #pack-m1-14-ex12
- Exercise 13: Count vowels → #pack-m1-14-ex13
- Exercise 14: Test if an integer is a palindrome → #pack-m1-14-ex14
- Exercise 15: Min and max of an array → #pack-m1-14-ex15
- Exercise 16: Searching in an array → #pack-m1-14-ex16
- Exercise 17: Binary search → #pack-m1-14-ex17
- Exercise 18: Quadratic-time algorithm → #pack-m1-14-ex18
- Exercise 19: Efficient sorting algorithm → #pack-m1-14-ex19
- Exercise 20: Alan Kay → #pack-m1-14-ex20
- Exercise 21: Dahl et Nygaard → #pack-m1-14-ex21
- Exercise 22: James Gosling → #pack-m1-14-ex22
- Exercise 23: domaines industriels → #pack-m1-14-ex23
- Exercise 24: Backus-Naur → #pack-m1-14-ex24
- Exercise 25: Cycles → #pack-m1-14-ex25
- Exercise 26: kibioctet → #pack-m1-14-ex26
- Exercise 27: doublons → #pack-m1-14-ex27
- Exercise 28: puissance → #pack-m1-14-ex28
- Exercise 29: occurrences d’un caractère spécifique → #pack-m1-14-ex29
- Exercise 30: recherche d’une clé → #pack-m1-14-ex30


---

## Sanitized extracts

_Each section header is the stable pack anchor._


## pack-m1-07-prerequisites

**Audit source:** `m1-07-Algorithms.en.sanitized.md`

## Prerequisites

In this course, concepts are presented thoroughly, with many examples and enrichment activities. However, we assume you have completed college-level mathematics (CEGEP) and that you have solid skills in formal reasoning.

In this first module, you will express solutions using **variables**, **loops**, and **branches** (conditionals). These are not advanced topics: you should already be familiar with them.

- Loops are implicit in computing a **sum** or a **dot product**.
- Variables in computer science are closely related to variables in algebra.
- Branches are basic notions from elementary logic.

You are responsible for ensuring you have the preparation required to follow INF 1220.

---

## pack-m1-07-what-is-an-algorithm

**Audit source:** `m1-07-Algorithms.en.sanitized.md`

### What is an algorithm?

An **algorithm** is a **finite**, **ordered** sequence of instructions that solves a problem or completes a specific task. It is a systematic method, expressed precisely, that yields a correct result when executed.

Everyday examples:
- a recipe (steps to cook a dish)
- instructions to assemble furniture

In computing, an algorithm might sort a list of numbers or compute the shortest path between two points.

---

## pack-m1-07-what-is-pseudocode

**Audit source:** `m1-07-Algorithms.en.sanitized.md`

### What is pseudocode?

**Pseudocode** is a way to write an algorithm using a simplified, structured language close to natural language. It is **not** meant to be executed directly by a computer. Its purpose is to describe the logic clearly, independently of any programming language.

Common conventions:
- `IF`, `THEN`, `ELSE` for conditions
- `FOR`, `WHILE` for loops
- `read` / `print` for input/output

Example: sum of two numbers

    read number1
    read number2
    sum ← number1 + number2
    print sum

Pseudocode lets you plan the logic first, then translate it into a language like Java.

---

## pack-m1-07-variables-and-values

**Audit source:** `m1-07-Algorithms.en.sanitized.md`

### Variables and values

A **variable** is a named storage location that contains a value. You can think of it as a labeled box: you put data in it, and the data may change while the algorithm runs.

Variables can hold different kinds of values (types), for example:
- **integer** (e.g., 5, -12, 0)
- **real number** (e.g., 3.14, -0.001)
- **boolean** (`true` / `false`)
- **string** (e.g., "hello", "INF1220")

In pseudocode, type is often implicit, but you must still understand what kind of value a variable holds to avoid mistakes. Variables should be named clearly (e.g., `age`, `sum`, `grades`). You assign values using an assignment operator such as `←` or `=`:

    age ← 18
    sum ← 0

Example: square a user-provided number

    read number
    square ← number * number
    print square

Good practice:
- initialize variables before using them (e.g., `sum ← 0` before accumulating)
- avoid using a variable before it has been assigned a value

---

## pack-m1-07-boolean-logic

**Audit source:** `m1-07-Algorithms.en.sanitized.md`

### Boolean logic

Boolean logic manipulates boolean values (`true` / `false`). It is essential for decisions (conditionals) and for controlling loops.

Main operators:

| A | B | NOT A | A AND B | A OR B |
|---|---|---|---|---|
| true | true | false | true | true |
| true | false | false | false | true |
| false | true | true | false | true |
| false | false | true | false | false |

Example 1: access control by age

    read age
    IF age >= 18 THEN
        print "Access granted"
    ELSE
        print "Access denied"
    END IF

You can combine conditions:

    read age
    read is_citizen
    IF age >= 19 AND is_citizen = true THEN
        print "You can vote"
    ELSE
        print "You cannot vote"
    END IF

Operator precedence (highest → lowest):
1. `NOT`
2. `AND`
3. `OR`

Use parentheses to remove ambiguity.

Example 2: check whether a number is in an interval

    read x
    IF x >= 10 AND x <= 20 THEN
        print "x is in [10, 20]"
    ELSE
        print "x is not in the interval"
    END IF

---

## pack-m1-07-programmer-notation

**Audit source:** `m1-07-Algorithms.en.sanitized.md`

### Programmer notation

For historical reasons, programmers often use symbolic operators:
- `AND` → `&&`
- `OR` → `||`
- `NOT` → `!`

This is common in Java and many other languages.

---

## pack-m1-07-the-loop

**Audit source:** `m1-07-Algorithms.en.sanitized.md`

## The loop

An algorithm usually takes input data and produces an output. For example, an algorithm that checks whether a number is even takes a number and outputs a boolean (`true`/`false`).

Many algorithms are **iterative**: they repeat a process. Intuitively, imagine painting a fence plank by plank. You need a way to remember where you are if you take a break. A “marker” indicates progress—this is the idea of an **iterator**.

In computing, we typically use an **integer counter** to track progress:
- to **increment** a counter usually means “add 1”
- to **decrement** usually means “subtract 1”

A **loop** repeats a task until a stopping condition becomes true (or until the loop condition becomes false).

Example: print numbers 1 to 10 (counter loop)

Java:

```java
for (int i = 1; i <= 10; i++) {
    System.out.println(i);
}
```

JavaScript:

```javascript
for (let i = 1; i <= 10; i++) {
    console.log(i);
}
```

Go:

```go
for i := 1; i <= 10; i++ {
    fmt.Println(i)
}
```

C++:

```cpp
for (int i = 1; i <= 10; i++) {
    std::cout << i << std::endl;
}
```

---

## pack-m1-07-array

**Audit source:** `m1-07-Algorithms.en.sanitized.md`

## Array

An **array** is a data structure that stores multiple elements (numbers, strings, etc.) in a single variable. Elements are accessed by an **index** (an integer position).

Indexing conventions vary:
- Many languages (C/Java/Python) start indexes at **0** (`array[0]` is the first element).
- Some contexts/languages start at **1** (more intuitive for some users).
You must know which convention is used in a given context.

Examples:

Java (fixed-size):

```java
int[] arr = new int[5]; // initialized with 0s
```

Java (literal initialization):

```java
int[] arr = new int[]{1, 2, 3};
```

JavaScript:

```javascript
let arr = Array(5).fill(0);
let arr2 = [1, 2, 3];
```

Go:

```go
arr := make([]int, 5)
arr2 := []int{1, 2, 3}
```

C++:

```cpp
int arr[5]{};
int arr2[]{1, 2, 3};
```

In these languages, `arr[0]` refers to the first element.

---

## pack-m1-07-average-example

**Audit source:** `m1-07-Algorithms.en.sanitized.md`

## Example: computing an average

Suppose we have an array of grades (e.g., 10.4, 12.6, 18.7, 5.0) and we want the average. Using 0-based indexing, the grades are `grades[0] … grades[3]`.

To keep the algorithm general, we use the **length** of the array rather than hard-coding “4”.

### Flowchart (conceptual)

```mermaid
graph TD
    A[Start] --> B[Initialize iterator = 0, average = 0]
    B --> C{iterator < length(grades)?}
    C -- True --> D["average = average + grades[iterator]"]
    D --> E[iterator = iterator + 1]
    E --> C
    C -- False --> F[average = average / length(grades)]
    F --> G[Print average]
    G --> H[End]
```

### Pseudocode

    Array of rational numbers: grades
    Variables:
      integer: iterator = 0
      rational: average = 0
    Output:
      rational: average

    WHILE iterator < length(grades) DO
        average = average + grades[iterator]
        iterator = iterator + 1
    END WHILE

    average = average / length(grades)

Note: ending the loop with `END WHILE` is not strictly required if indentation is unambiguous, but you must be clear about where loops begin and end.

### Translation to real code (example in Java)

```java
double[] grades = {10.4, 12.6, 18.7, 5.0};
double sum = 0;
for (int i = 0; i < grades.length; i++) {
    sum += grades[i];
}
double average = sum / grades.length;
System.out.println(average);
```

The structure matches the pseudocode: initialize sum to zero, iterate over indices, accumulate, then divide by the number of elements.

---

## pack-math-logic

**Audit source:** `Rappel mathématique _ INF 1220 - Introduction à la programmation.html`

1.1. Les propositions #Une proposition mathématique est un énoncé dont on peut dire sans ambiguïté si elle est vraie ou fausse. Le processus qui consiste à déterminer si une proposition mathématique est vraie ou fausse est l’objet du calcul propositionnel ou calcul des propositions et fait partie de la logique mathématique. Le résultat d’un calcul propositionnel est donc l’attribution d’une valeur de vérité à une proposition. Ainsi, l’énoncé « Le cours INF1220 figure parmi les cours dispensés à la TELUQ au trimestre d’hiver 2021 » est une proposition mathématique et sa valeur de vérité est « vrai ». La proposition « Le cours INF1220 est mon meilleur cours » n’est pas une proposition mathématique. Dans notre contexte, quand nous parlons de proposition, nous parlons de proposition mathématique. 1.1.1. Table des valeurs de vérités des propositions #Tableau 1 : Table de vérités et connecteurs logiques Cette table de vérité présente les valeurs logiques des propositions \( p \), \( q \) et de plusieurs connecteurs logiques pour toutes leurs combinaisons possibles. La colonne \( \neg p \) indique la négation de \( p \), vraie lorsque \( p \) est faux. Le connecteur \( p \vee q \) (ou) est vrai si au moins l’une des propositions est vraie. Le ou exclusif \( p \oplus q \) est vrai uniquement si exactement une des propositions est vraie. Le et \( p \wedge q \) est vrai seulement si les deux propositions sont vraies. L’implication \( p \Rightarrow q \) est fausse uniquement si \( p \) est vrai et \( q \) est faux. Enfin, la biconditionnelle \( p \Leftrightarrow q \) est vraie lorsque \( p \) et \( q \) ont la même valeur logique. Chaque ligne correspond à une combinaison des valeurs de vérité de \( p \) et \( q \), illustrant ainsi le comportement de ces connecteurs. 1.1.1. Table des valeurs de vérités des propositions #Tableau 1 : Table de vérités et connecteurs logiques Cette table de vérité présente les valeurs logiques des propositions \( p \), \( q \) et de plusieurs connecteurs logiques pour toutes leurs combinaisons possibles. La colonne \( \neg p \) indique la négation de \( p \), vraie lorsque \( p \) est faux. Le connecteur \( p \vee q \) (ou) est vrai si au moins l’une des propositions est vraie. Le ou exclusif \( p \oplus q \) est vrai uniquement si exactement une des propositions est vraie. Le et \( p \wedge q \) est vrai seulement

[…truncated…]

---

## pack-math-sets

**Audit source:** `Rappel mathématique _ INF 1220 - Introduction à la programmation.html`

1.2. Les ensembles #Un ensemble est une collection d’objets. Si on appelle \( E \) cette collection, alors pour chacun de ces objets, on peut affirmer qu’il appartient à \( E \). On peut déterminer \( E \) en énumérant ses éléments, par exemple \( E = \{ o_1, o_2, \dots \} \), où \( o_i \) est un des objets de la collection (et où on admet que pour tout objet de la collection, il y a un \( o_i \) qui lui soit identique). On dit alors qu’on a défini \( E \) en extension. Un objet \( o_i \) est appelé un élément de \( E \). On note \( o_i \in E \). Étant donné un objet arbitraire, c’est-à-dire une chose quelconque, on est capable de dire si oui ou non cette chose appartient à \( E \). Si nous notons la chose en question \( o \) et qu’elle n’appartient pas à \( E \), nous traduisons cela par \( o \notin E \). Une autre façon de déterminer un ensemble est de donner une propriété qui caractérise ses éléments. Par exemple, la collection de toutes les personnes qui sont inscrites à la TELUQ pour suivre le cours INF1220 pour le trimestre d’hiver 2021 à la date du 1er mars 2021 est un ensemble. Nous pouvons le noter \( T \). On convient dans ce cas d’écrire \( T = \{ o \mid o \text{~est~inscrit} \} \). Le symbole \( \mid \) se lit « tel que ». « Être inscrit à la TELUQ pour suivre le cours INF1220 pour le trimestre d’hiver 2021 à la date du 1er mars 2021 » est la propriété caractéristique de l’ensemble \( T \) (ou des éléments de cet ensemble). Les nombres entiers positifs forment un ensemble ; c’est l’ensemble des entiers naturels. On le note \( \mathbb{N} \). \( \mathbb{N} = \{ 0, 1, \dots \} \). Un ensemble peut être fini, comme l’ensemble \( T \). Un ensemble peut être infini, comme l’ensemble \( \mathbb{N} \). On admet qu’il existe un ensemble qui ne contient aucun élément. On appelle cet ensemble, ensemble vide. On le note couramment \( \{ \} \) ou \( \emptyset \). Un singleton est un ensemble qui a un seul élément. On admet aussi que si l’on ajoute un élément d’un ensemble \( E \) à ce même ensemble \( E \), on ne change pas l’ensemble \( E \). On considère de ce fait, qu’un ensemble est donné par une collection

[…truncated…]

---

## pack-math-relations

**Audit source:** `Rappel mathématique _ INF 1220 - Introduction à la programmation.html`

1.3. Relation binaire #Une relation binaire \( R \) est un ensemble défini par la donnée de deux ensembles \( A \) et \( B \) et d’une règle qui permet d’associer certains éléments de \( A \) à certains éléments de \( B \). \( R \) est un sous-ensemble du produit cartésien \( A \times B \) de \( A \) et de \( B \). La règle associée à une relation est aussi appelée lien verbal. Le lien verbal est une proposition. On peut définir une relation en compréhension par \( R = \{ (a, b) \in A \times B \mid \text{le lien verbal soit vérifié pour } a \text{ et } b \} \). Au lieu de noter \( (a, b) \in R \), on note simplement \( a R b \) et on lit \( a \) en relation avec \( b \). \( b \) est l’image de \( a \) par la relation \( R \) et \( a \) est l’antécédent de \( b \) pour la relation \( R \). 1.3.1. Propriété d’une relation binaire #Soit \( R \) une relation binaire. Lorsque les ensembles de départ et d’arrivée sont identiques, c’est-à-dire tous égaux à \( A \), on dit simplement que \( R \) est une relation définie sur \( A \). Soit \( A \) un ensemble et \( R \) une relation binaire définie sur \( A \). \( R \) peut avoir les propriétés suivantes : 1.3.1.1. Réflexivité #\( R \) est réflexive si \( \forall a \in A, a R a \). Exemple : la relation de divisibilité \( R \) dans \( \mathbb{N} \) (\( a R b \) ssi \( a \) divise \( b \)) est réflexive. Question : donnez un autre exemple de relation réflexive. RéponseLa relation d'ordre naturel \( R \) sur \( \mathbb{N} \) définie par \( a R b \) ssi \( a \leq b \) est réflexive.1.3.1.2. Symétrie #\( R \) est symétrique ssi \( \forall a \in A, \forall b \in B, a R b \Rightarrow b R a \). Exemple : soit \( m \in \mathbb{N}^* \). La relation \( R \) définie sur \( \mathbb{N} \) par \( a R b \) ssi \( a \) et \( b \) ont le même reste dans la division euclidienne par \( m \) est symétrique. 1.3.1.3. Transitivité #\( R \) est transitive ssi pour \( a, b, c \in A \), \( a R b \)

[…truncated…]

---

## pack-math-numbers

**Audit source:** `Rappel mathématique _ INF 1220 - Introduction à la programmation.html`

1.4. L’ensemble des entiers naturels \( \mathbb{N} \) et les autres ensembles de nombres #Il faut noter que les entiers naturels forment un ensemble particulier. Pour illustrer le lien étroit qu’il y a entre la théorie des ensembles et les entiers naturels, il faut savoir qu’on peut construire l’ensemble des entiers naturels en procédant comme suit : \( 0 = \emptyset \), \( 1 = \text{successeur de } 0 \), c’est-à-dire \( 1 = \{0\} \), \( 2 = \text{successeur de } 1 \), c’est-à-dire \( 2 = \{0, 1\} \), etc. Commençons par voir de façon générale les lois de composition sur un ensemble. 1.4.1. Lois de composition dans un ensemble #Soit \( E \) et \( G \) deux ensembles. Une loi de composition \( T \) dans l’ensemble \( E \) est une fonction de \( E \times E \) vers \( G \) qui à tout couple \( (a, b) \) d’éléments de \( E \) associe un unique élément \( c \) de \( G \) tel que \( c = a T b \). Soit \( E \) un ensemble muni d’une loi \( T \). 1.4.1.1. Ensemble stable par une loi #Si \( \forall a, b \in E \), \( a T b \in E \), alors la loi \( T \) est interne sur \( E \). On dit aussi que \( E \) est stable par la loi \( T \). On note \( (E, T) \) pour signifier que \( E \) est muni de la loi interne \( T \). Par exemple, l’addition est interne à l’ensemble des entiers naturels \( \mathbb{N} \). 1.4.1.2. Élément neutre pour une loi #Un élément \( e \) de \( E \) est un élément neutre pour \( T \) ssi pour tout élément \( a \) de \( E \), \( a T e = e T a = a \). Exemple : 0 est l’élément neutre pour l’addition \( + \) sur l’ensemble \( \mathbb{N} \) des entiers naturels : pour tout entier naturel \( n \), on a \( n + 0 = 0 + n = n \). Il en est de même pour 1 qui est l’élément neutre pour la multiplication \( \times \) sur l’ensemble \( \mathbb{N} \) des entiers naturels : pour tout entier naturel \( n \), on a \( n \times 1 = 1 \times n = n \). Question : existe-t-il un élément neutre pour la division \( \div \) sur l’ensemble \(

[…truncated…]

---

## pack-math-series

**Audit source:** `Rappel mathématique _ INF 1220 - Introduction à la programmation.html`

2.3. Suites et séries numériques réelles #Une suite numérique réelle est une application \( u : \mathbb{N} \to \mathbb{R} \), \( n \mapsto u(n) \). On note souvent \( u(n) \), l’image par \( n \) de \( u \), plus simplement \( u_n \). La suite \( u \) est souvent notée \( (u_n)_{n \in \mathbb{N}} \). Le terme \( u_n \) s’appelle le terme général de la suite. Il arrive quelquefois qu’une suite soit définie seulement sur une partie de \( \mathbb{N} \). Dans ce cas, on considère qu’elle est définie partout sur \( \mathbb{N} \) et qu’elle est nulle pour les termes pour lesquels elle n’est pas explicitement définie. Par exemple, si on considère la suite \( u \) définie par \( u_n = 1/n \) pour \( n > 0 \) sans d’autres précisions, on peut toujours supposer que \( u_0 = 0 \). Une suite n’est intéressante que s’il y a une façon de déterminer, pour un entier \( n \) quelconque, le terme \( u_n \) de la suite; on parle alors de suite logique. Une suite logique peut être donnée par une expression de \( u_n \) en fonction de \( n \); \( u_n = f(n) \) où \( f \) est une fonction avec \( D_f = \mathbb{N} \). Une suite logique peut être donnée par une relation entre les termes de la suite. Par exemple, \( u_n \) peut être une fonction de \( u_{n-1} \); \( u_n = f(u_{n-1}) \) où \( f \) est une fonction et il y a au moins un terme de la suite connu (il existe \( n_0 \) tel que \( u_{n_0} \) soit connu); dans ce cas, on parle de suite récurrente. Un exemple de suite est (suite de Fibonacci) \( u_0 = 0 \), \( u_1 = 1 \) et \( u_n = u_{n-1} + u_{n-2} \) pour \( n \geq

[…truncated…]

---

## pack-m1-08-design

**Audit source:** `m1-08-Les algorithmes-conception et syntaxe.md`

Concevoir un algorithme
-----------------------------------------------------

Pour concevoir un algorithme, il convient d’analyser minutieusement le problème en identifiant les entrées, les sorties et les étapes de traitement nécessaires pour obtenir les résultats souhaités. Un algorithme se présente comme une suite logique d’instructions qu’un programmeur peut adapter à un langage comme Java, C++ ou Python. La démarche de conception suit généralement ces étapes :

Étape 1 : lire et comprendre l’énoncé du problème à résoudre.  
Étape 2 : définir les sorties (résultats attendus), les entrées (données initiales) et le traitement (relations permettant de passer des entrées aux sorties).  
Étape 3 : rédiger l’algorithme en pseudo-code, en respectant une structure claire et compréhensible.

---

## pack-m1-08-syntax

**Audit source:** `m1-08-Les algorithmes-conception et syntaxe.md`

Syntaxe d’un algorithme
----------------------------------------------------

La syntaxe d’un algorithme repose sur des conventions souples, contrairement aux langages de programmation qui imposent des règles strictes. Le pseudo-code privilégie la clarté et la précision des instructions, en s’appuyant sur des structures standardisées. Si une étape semble ambiguë ou trop complexe, il est souvent préférable de la décomposer en sous-étapes pour en faciliter la compréhension.

### Les entrées, variables et sorties

Un algorithme débute par la déclaration des entrées, c’est-à-dire les données fournies directement (comme un texte à analyser ou des données financières) ou saisies par un utilisateur (via un clavier, une souris, etc.). Viennent ensuite les variables, qui portent un nom et une valeur, comme une variable `x` valant 1. Ces valeurs peuvent évoluer au fil du traitement. Les variables, utilisées pour stocker des informations intermédiaires, se déclinent en divers types : chaînes de caractères, entiers, nombres décimaux, etc. Enfin, les sorties correspondent aux résultats finaux du traitement, transmis à l’utilisateur ou à d’autres algorithmes. Un problème complexe peut en effet être résolu par plusieurs algorithmes interconnectés, un concept que nous relierons plus tard aux fonctions dans les langages de programmation.

### Les opérations

Un algorithme se décrit comme une séquence d’opérations, par exemple additionner deux nombres ou incrémenter une variable. Les opérations disponibles dépendent du modèle de calcul adopté, mais on presume généralement que les opérations mathématiques de base (addition, soustraction, multiplication, comparaison) sont prises en charge.

Les notations varient selon les conventions. Une multiplication peut s’écrire `x * y`, `x × y` ou simplement `x y`. De même, pour assigner la valeur 1 à une variable `x`, on peut utiliser `x ← 1` ou `x = 1`. Cependant, dans certains contextes, `x = 1` pourrait indiquer une comparaison (« x vaut-il 1 ? »). Pour lever l’ambiguïté, une notation comme `x == 1` est parfois préférée pour les comparaisons, en s’inspirant de langages de programmation. L’essentiel reste que chaque opération soit exprimée de manière claire et sans équivoque pour le lecteur.

---

## pack-m1-08-io

**Audit source:** `m1-08-Les algorithmes-conception et syntaxe.md`

### Les entrées, variables et sorties

Un algorithme débute par la déclaration des entrées, c’est-à-dire les données fournies directement (comme un texte à analyser ou des données financières) ou saisies par un utilisateur (via un clavier, une souris, etc.). Viennent ensuite les variables, qui portent un nom et une valeur, comme une variable `x` valant 1. Ces valeurs peuvent évoluer au fil du traitement. Les variables, utilisées pour stocker des informations intermédiaires, se déclinent en divers types : chaînes de caractères, entiers, nombres décimaux, etc. Enfin, les sorties correspondent aux résultats finaux du traitement, transmis à l’utilisateur ou à d’autres algorithmes. Un problème complexe peut en effet être résolu par plusieurs algorithmes interconnectés, un concept que nous relierons plus tard aux fonctions dans les langages de programmation.

---

## pack-m1-08-operations

**Audit source:** `m1-08-Les algorithmes-conception et syntaxe.md`

### Les opérations

Un algorithme se décrit comme une séquence d’opérations, par exemple additionner deux nombres ou incrémenter une variable. Les opérations disponibles dépendent du modèle de calcul adopté, mais on presume généralement que les opérations mathématiques de base (addition, soustraction, multiplication, comparaison) sont prises en charge.

Les notations varient selon les conventions. Une multiplication peut s’écrire `x * y`, `x × y` ou simplement `x y`. De même, pour assigner la valeur 1 à une variable `x`, on peut utiliser `x ← 1` ou `x = 1`. Cependant, dans certains contextes, `x = 1` pourrait indiquer une comparaison (« x vaut-il 1 ? »). Pour lever l’ambiguïté, une notation comme `x == 1` est parfois préférée pour les comparaisons, en s’inspirant de langages de programmation. L’essentiel reste que chaque opération soit exprimée de manière claire et sans équivoque pour le lecteur.

---

## pack-m1-08-example-vowels

**Audit source:** `m1-08-Les algorithmes-conception et syntaxe.md`

Compter le nombre de voyelles d’un mot entrées au clavier
-----------------------------------------------------------------------------------------------------------------------------

L’algorithme suivant compte le nombre de voyelles saisies :

    Entrées :
      Chaîne de caractères : chaine = ""
    Sorties :
      Entier : nbVoyelle = 0
    Imprimer à l'écran "Veuillez entrer un mot au clavier suivi de la touche entrée"
    Saisir le mot au clavier et assigner à la variable chaine
    POUR TOUT caractère c dans chaine FAIRE
        SI c == 'a' OU c == 'e' OU c == 'i' OU c == 'o' OU c == 'u' OU c == 'y' ALORS
            nbVoyelle = nbVoyelle + 1
        FIN SI
    FIN POUR
    

Initialement, une variable chaine est définie comme une chaîne vide, et une variable nbVoyelle est initialisée à 0 pour compter les voyelles. L’algorithme affiche un message invitant l’utilisateur à entrer un mot suivi de la touche Entrée, puis stocke l’entrée dans chaine. Une boucle (POUR TOUT caractère c dans chaine FAIRE) parcourt chaque caractère c de la chaîne. Pour chaque caractère, une condition vérifie si c est une voyelle (a, e, i, o, u ou y) en utilisant une série de comparaisons avec l’opérateur OU. Si le caractère est une voyelle, nbVoyelle est incrémenté de 1. À la fin de la boucle, nbVoyelle contient le nombre total de voyelles dans la chaîne.

Le compteur de voyelles est un outil interactif conçu pour t’aider à comprendre comment un algorithme traite une chaîne de caractères pour compter ses voyelles. Commence par saisir un mot ou une phrase dans le champ de texte, par exemple « bonjour ». Clique sur le bouton « Prochaine étape » pour exécuter l’algorithme pas à pas. À chaque clic, une ligne du pseudocode s’illumine, et une explication apparaît dans la zone de journalisation en bas. Tu verras aussi l’état actuel : la chaîne saisie, le caractère en cours d’analyse et le nombre de voyelles comptées. Si tu veux recommencer, clique sur « Réinitialiser » pour effacer les résultats et repartir de zéro. Assure-toi que ta saisie n’est pas vide, sinon un message te demandera de corriger.

Cet outil vous permet de suivre la logique de l’algorithme de manière visuelle. Le pseudocode, affiché à gauche, détaille chaque étape : initialisation des variables (comme la chaîne et le compteur de voyelles), lecture de la saisie, parcours de chaque caractère et vérification s’il s’agit d’une voyelle (a, e, i, o, u, y). En avançant étape par étape, tu peux observer comment l’algorithme « pense » pour résoudre le problème. Prenez le temps de lire les messages du journal pour comprendre ce qui se passe à chaque moment. Cet exercice est parfait pour t’entraîner à traduire un problème en une série d’instructions claires, une compétence essentielle en programmation.

---

## pack-m1-09-jump

**Audit source:** `m1-09-Les algorithmes - les structures de contrôle.md`

Le saut
---------------------

Le saut est une structure de contrôle fondamentale en informatique qui permet de modifier le flux d’exécution d’un algorithme en redirigeant l’exécution vers une autre partie du programme. Contrairement aux structures comme les embranchements (qui choisissent entre plusieurs chemins selon une condition) ou les boucles (qui répètent un bloc d’instructions), le saut est une instruction explicite qui transfère immédiatement le contrôle à une position spécifique dans le code, souvent marquée par une étiquette ou une adresse. Un saut peut être inconditionnel, où l’exécution est toujours redirigée vers une nouvelle position, ou conditionnel, où le saut dépend d’une condition booléenne.

Un saut inconditionnel redirige l’exécution vers une étiquette ou une ligne spécifique sans vérifier de condition. En pseudo-code, cela peut être représenté ainsi :

    ÉTIQUETTE debut
    écrire "Bonjour"
    SAUTER À debut
    

Dans cet exemple, l’algorithme affiche “Bonjour” et saute immédiatement à l’étiquette debut, créant une boucle infinie. Bien que rarement utilisé seul en pseudo-code, ce type de saut est courant dans les langages de bas niveau pour organiser le flux du programme

---

## pack-m1-09-branching

**Audit source:** `m1-09-Les algorithmes - les structures de contrôle.md`

L’embranchement comme structure de contrôle
-------------------------------------------------------------------------------------------------

Un saut conditionnel (ou embranchement) dépend d’une condition booléenne. Si la condition est vraie, l’exécution saute à une étiquette donnée ; sinon, elle continue séquentiellement. Voici un exemple en pseudo-code :

    lire nombre
    SI nombre < 0 ALORS
        SAUTER À negatif
    FIN SI
    écrire "Le nombre est positif ou nul"
    SAUTER À fin
    ÉTIQUETTE negatif
    écrire "Le nombre est négatif"
    ÉTIQUETTE fin
    

En pratique, ces structures correspondent à poser des questions avec la syntaxe suivante : SI conditions ALORS opérations FIN SI. Il peut y avoir plusieurs conditions dans une structure de contrôle et la logique booléenne est utilisée pour les construire. Par exemple, SI a est égal 0 ET b est égal 1 ALORS faire c FIN SI.

Dans la notion de pseudo-code, il est également possible de faire une suite de structures de contrôle avec la syntaxe suivante : SI conditionA ALORS opérations SINON SI conditionB ALORS opérations SINON SI conditionC ALORS \[et ainsi de suite\] FIN SI.

Voici un exemple en pseudo-code illustrant une suite de structures de contrôle avec plusieurs conditions pour classer un score obtenu à un examen :

    lire score
    SI score ≥ 90 ALORS
        écrire "Note : A"
    SINON SI score ≥ 80 ALORS
        écrire "Note : B"
    SINON SI score ≥ 70 ALORS
        écrire "Note : C"
    SINON SI score ≥ 60 ALORS
        écrire "Note : D"
    SINON
        écrire "Note : F"
    FIN SI
    

Dans cet exemple, l’algorithme lit une variable score (un nombre entier représentant un score d’examen). Il utilise une série de conditions pour déterminer la note correspondante :

*   Si score est supérieur ou égal à 90, la note est “A”.
*   Sinon, si score est supérieur ou égal à 80, la note est “B”.
*   Sinon, si score est supérieur ou égal à 70, la note est “C”.
*   Sinon, si score est supérieur ou égal à 60, la note est “D”.
*   Sinon (pour tout score inférieur à 60), la note est “F”.

Chaque condition est évaluée séquentiellement, et dès qu’une condition est vraie, l’algorithme exécute l’opération associée (afficher la note) et sort de la structure avec FIN SI. Si aucune condition n’est vraie, l’opération par défaut (afficher “Note : F”) est exécutée.

Considérons l’exemple suivant. Il s’agit d’un outil interactif qui t’aide à comprendre comment un algorithme utilise des conditions pour classer une personne selon son âge. Pour commencer, saisis un âge entier positif dans le champ prévu, par exemple « 25 ». Ensuite, clique sur « Prochaine étape » pour exécuter l’algorithme étape par étape. À chaque clic, une ligne du pseudocode s’illumine, et un message explicatif apparaît dans la zone de journalisation en bas. Tu verras également l’état mis à jour : l’âge saisi et la catégorie déterminée (comme « Vous êtes un adulte »). Si tu veux recommencer, clique sur « Réinitialiser » pour effacer les résultats. Attention, l’âge doit être un nombre entier positif, sinon un message te demandera de corriger.

Cet outil vous permet de suivre le raisonnement de l’algorithme de manière claire. Le pseudocode, affiché à gauche, utilise une structure conditionnelle (SI, SINON SI, SINON) pour évaluer l’âge et assigner une catégorie : enfant (≤ 10 ans), adolescent (> 10 et < 18 ans), adulte (≥ 18 et < 65 ans) ou personne âgée (≥ 65 ans). En progressant dans les étapes, observe comment l’algorithme teste chaque condition et choisit la bonne catégorie. Lisez attentivement les messages du journal pour comprendre les décisions prises.

---

## pack-m1-09-loop

**Audit source:** `m1-09-Les algorithmes - les structures de contrôle.md`

La boucle comme structure de contrôle
--------------------------------------------------------------------------------------

Il arrive régulièrement dans la résolution d’un problème qu’il est nécessaire de réaliser à plusieurs reprises une ou des opérations sur un ensemble de données. Par exemple, supposons qu’il est nécessaire de trouver le plus petit nombre dans un tableau d’entiers. Il sera forcément nécessaire d’itérer dans le tableau, une ligne à la fois, et de comparer les nombres entre eux. Pour ce faire, nous utiliserons deux éléments de syntaxe, soit le TANT QUE \_ FAIRE ou bien le POUR TOUT \_ FAIRE. Voici deux exemples de l’utilisation de ces deux approches :

Pseudocode 1 : Boucle POUR TOUT

    Entrées :
    Tableau d'entiers : tableau[100]
    
    Sorties :
    Entier minimum
    
    minimum = tableau[0]
    POUR TOUT Entier e de tableau FAIRE
        SI e < minimum ALORS
            minimum = e;
        FIN SI
    FIN POUR TOUT
    

Ce pseudocode décrit un algorithme pour trouver la valeur minimale dans un tableau d’entiers de taille 100. L’algorithme commence par initialiser la variable minimum à la première valeur du tableau (tableau\[0\]), en supposant que le tableau n’est pas vide. Ensuite, une boucle (POUR TOUT Entier e de tableau FAIRE) parcourt chaque élément e du tableau. À chaque itération, si l’élément e est inférieur à la valeur actuelle de minimum, alors minimum est mis à jour avec la valeur de e (minimum = e). À la fin de la boucle, minimum contient la plus petite valeur du tableau, qui est retournée comme résultat.

Pseudocode 2 : Boucle TANT QUE

    Entrées :
    Tableau d'entiers : tableau[100]
    
    Sorties :
    Entier minimum
    
    minimum = tableau[0]
    Entier iterateur = 0;
    TANT QUE iterateur < 100 FAIRE
        SI tableau[iterateur] < minimum ALORS
            minimum = tableau[iterateur];
        FIN SI
        iterateur = iterateur + 1;
    FIN TANT QUE
    

Ce pseudocode décrit un algorithme pour trouver la valeur minimale dans un tableau d’entiers de taille 100. Une variable minimum est initialisée avec la première valeur du tableau (tableau\[0\]), supposant que le tableau n’est pas vide. Une variable iterateur est initialisée à 0 pour suivre la position dans le tableau. La boucle (TANT QUE iterateur < 100 FAIRE) parcourt le tableau tant que iterateur est inférieur à 100. À chaque itération, si l’élément à l’indice iterateur (tableau\[iterateur\]) est inférieur à minimum, alors minimum est mis à jour avec cette valeur. Ensuite, iterateur est incrémenté de 1 (iterateur = iterateur + 1) pour passer à l’élément suivant. À la fin de la boucle, minimum contient la plus petite valeur du tableau, qui est retournée.

Au niveau fondamental, une boucle peut être vue comme un saut conditionnel dans le flux d’exécution d’un algorithme. Un saut conditionnel est une instruction qui, en fonction d’une condition, redirige l’exécution vers une autre partie du programme. Dans le cas d’une boucle, ce saut ramène l’exécution au début du bloc d’instructions tant que la condition associée à la boucle reste vraie.

Prenons l’exemple de la boucle TANT QUE. La condition iterateur < 100 est évaluée à chaque itération. Si elle est vraie, l’algorithme exécute le corps de la boucle (comparaison et mise à jour de minimum, incrémentation de iterateur), puis retourne au début de la boucle pour réévaluer la condition. Ce retour au début est un saut conditionnel : l’algorithme “saute” en arrière dans le code pour répéter le processus. Lorsque la condition devient fausse (quand iterateur atteint 100), le saut n’a plus lieu, et l’exécution continue après la boucle.

De même, dans la boucle POUR TOUT du Pseudocode 1, bien que la syntaxe soit plus abstraite, le mécanisme sous-jacent est similaire. La boucle parcourt chaque élément du tableau, ce qui peut être traduit en une série de sauts conditionnels gérés implicitement : après avoir traité un élément, l’algorithme “saute” à l’élément suivant tant qu’il reste des éléments à traiter.

---

## pack-m1-09-composition

**Audit source:** `m1-09-Les algorithmes - les structures de contrôle.md`

Composition
-----------------------------

Dans la pratique, un algorithme peut comporter plusieurs structures de contrôle itératives, plusieurs structures de contrôle alternatives et plusieurs opérations. On peut les combiner de diverses manières. Il est possible, par exemple, d’avoir une boucle TANT QUE au sein d’une autre boucle TANT QUE.

    TANT QUE x > 0 FAIRE
      TANT QUE x > 10 FAIRE
         x = x - 1
      FIN TANT QUE
    FIN TANT QUE
    

Ce pseudocode décrit une structure de boucles imbriquées qui modifie la valeur de la variable x jusqu’à ce qu’elle devienne inférieure ou égale à 0. La boucle externe (TANT QUE x > 0 FAIRE) continue tant que x est strictement positif. À l’intérieur, la boucle interne (TANT QUE x > 10 FAIRE) s’exécute uniquement si x est supérieur à 10, et dans ce cas, elle décrémente x de 1 à chaque itération (x = x - 1). Une fois que x devient inférieur ou égal à 10, la boucle interne s’arrête, mais la boucle externe ne se termine pas immédiatement, car elle vérifie seulement si x > 0. Cependant, comme il n’y a aucune instruction dans la boucle externe pour modifier x lorsque x ≤ 10, le programme entre dans une boucle infinie si x est compris entre 1 et 10 inclus. Si x est initialement supérieur à 10, il sera décrémenté jusqu’à atteindre 10, puis le programme se bloquera. Si x est initialement inférieur ou égal à 0, aucune des boucles ne s’exécute.

---

## pack-m1-09-ending

**Audit source:** `m1-09-Les algorithmes - les structures de contrôle.md`

La fin d’un algorithme
--------------------------------------------------

Un algorithme continue à s’exécuter tant qu’il reste des operations à faire. L’algorithme prend fin lorsque nous rencontrons la fin du pseudo-code ou lorsque le programmeur invoque la fin spécifiquement. Dans l’exemple suivant, le programmeur demande à ce que l’on cesse l’exécution dès que la valeur 5 est rencontrée.

    x = 0
    TANT QUE x < 10 ALORS
       ajoute un à x
       SI x == 5 ALORS TERMINE
    FIN TANT QUE
    AFFICHE x
    

La valeur x ne sera donc jamais affichée.

Il arrive aussi qu’un pseudo-code doit retourner une valeur. Par convention, dès que la valeur attendue est retournée, l’algorithme prend fin. Ainsi donc, dans le cas suivant, la valeur 5 sera retournée.

    x = 0
    TANT QUE x < 10 ALORS
       ajoute un à x
       SI x == 5 ALORS RETOURNE x
    FIN TANT QUE
    RETOURNE x

---

## pack-m1-09-tracing

**Audit source:** `m1-09-Les algorithmes - les structures de contrôle.md`

Exécution d’un pseudo-code
---------------------------------------------------------------

Pour comprendre un pseudo-code que vous venez de recevoir, ou pour tester un pseudo-code que vous venez de créer, il est essentiel de l’exécuter. Quand on exécute un pseudo-code, on se contente de lire les consignes logiques.

Prenons un exemple:

    Variable test = 0
    
    TANT QUE test < 100
      test = test + 22
    FIN TANT QUE
    
    retourne test
    

mermaid.initialize({flowchart:{useMaxWidth:!0},theme:"default"})

graph TD
    A\[Début\] --> B\[Initialiser test = 0\]
    B --> C{test < 100 ?}
    C -- Vrai --> D\[test = test + 22\]
    D --> C
    C -- Faux --> E\[Retourner test\]
    E --> F\[Fin\]

1.  Je débute le pseudo-code avec la valeur 0 stockée dans la variable test.
2.  J’entre dans la boucle TANT QUE.
3.  J’ajoute 22 à la variable test, le résultat est 22.
4.  J’entre dans la boucle TANT QUE.
5.  J’ajoute 22 à la variable test, le résultat est 44.
6.  J’entre dans la boucle TANT QUE.
7.  J’ajoute 22 à la variable test, le résultat est 66.
8.  J’entre dans la boucle TANT QUE.
9.  J’ajoute 22 à la variable test, le résultat est 88.
10.  J’entre dans la boucle TANT QUE.
11.  J’ajoute 22 à la variable test, le résultat est 110.
12.  Je quitte la boucle TANT QUE.
13.  Je retourne la valeur stockée dans la variable test, soit 110.

Vous devez absolument être capable de faire de telles exécutions. Dans certains cas, votre pseudo-code va dépendre de paramètres: il faut alors exécuter le pseudo-code plus d’une fois, sur plusieurs cas de test. Dans certains cas, le pseudo-code peut prendre trop d’étapes pour qu’un humain puisse l’exécuter entièrement : vous devriez au moins en faire une partie.

---

## pack-m1-10-tsp-nearest-neighbor

**Audit source:** `m1-10-Les problèmes difficiles.md`

Problème du voyageur de commerce (TSP)
--------------------------------------

### Pseudocode (Approche du plus proche voisin)

Entrées :
  Liste de villes : villes\[n\]
  Matrice des distances : distances\[n\]\[n\]

Sorties :
  Liste ordonnée des villes : trajet

Initialiser trajet comme une liste vide
Choisir une ville de départ aléatoire et l’ajouter à trajet
Marquer la ville de départ comme visitée
TANT QUE toutes les villes ne sont pas visitées FAIRE
    Trouver la ville non visitée la plus proche de la dernière ville dans trajet
    Ajouter cette ville à trajet
    Marquer cette ville comme visitée
FIN TANT QUE
Ajouter la ville de départ à la fin de trajet pour boucler
RETOURNER trajet, Distance totale
            

### Tableau des distances (km)

Ville

Montréal

Québec

Laval

Gatineau

Longueuil

Montréal

\-

250

20

200

15

Québec

250

\-

240

450

245

Laval

20

240

\-

210

30

Gatineau

200

450

210

\-

210

Longueuil

15

245

30

210

\-

Commencer Réinitialiser

---

## pack-m1-10-distance-table

**Audit source:** `m1-10-Les problèmes difficiles.md`

### Tableau des distances (km)

Ville

Montréal

Québec

Laval

Gatineau

Longueuil

Montréal

\-

250

20

200

15

Québec

250

\-

240

450

245

Laval

20

240

\-

210

30

Gatineau

200

450

210

\-

210

Longueuil

15

245

30

210

\-

Commencer Réinitialiser

---

## pack-m1-11-big-o

**Audit source:** `m1-11-Complexité algorithmique.md`

### Notation grand-O

La notation \\( O(f(n)) \\) signifie que, pour des entrées de taille \\( n \\), l’algorithme effectue au plus un nombre d’opérations proportionnel à \\( f(n) \\) (à une constante près). On ne s’intéresse qu’au comportement pour de grandes valeurs de \\( n \\), et on ignore les détails d’implémentation ou les constantes cachées.

On considère souvent que l’accès à un élément d’un tableau par son index a une complexité \\( O(1) \\) puisqu’il s’agit d’une seule opération. Les operations arithmétique (+, -, etc.) ont aussi une complexité \\( O(1) \\).

---

## pack-m1-11-examples

**Audit source:** `m1-11-Complexité algorithmique.md`

### Exemples d’algorithmes en \\( O(n) \\)

Un algorithme est en \\( O(n) \\) si le nombre d’opérations croît linéairement avec la taille de l’entrée. Par exemple, parcourir un tableau pour calculer la somme de ses éléments :

    somme = 0
    POUR i de 0 à n-1
        somme = somme + tableau[i]
    FIN POUR
    

Une variable somme est initialisée à 0 pour accumuler le résultat. La boucle (POUR i de 0 à n-1) parcourt chaque indice i du tableau, et à chaque itération, la valeur de l’élément tableau\[i\] est ajoutée à somme (`somme = somme + tableau[i]`). À la fin de la boucle, somme contient la somme totale des éléments du tableau.

Ici, chaque élément est visité une seule fois, donc le temps d’exécution est proportionnel à \\( n \\).

---

## pack-m1-11-binary-search

**Audit source:** `m1-11-Complexité algorithmique.md`

### Recherche dans un tableau trié

Lorsqu’un tableau est trié, on peut utiliser la recherche dichotomique (ou recherche binaire) pour trouver rapidement un élément. Cette méthode consiste à comparer la valeur recherchée à l’élément du milieu du tableau : si la valeur est plus petite, on recommence la recherche dans la moitié gauche ; sinon, dans la moitié droite. On répète jusqu’à trouver l’élément ou à épuiser le tableau.

Voici un exemple de pseudocode pour la recherche binaire :

    DEBUT
        debut ← 0
        fin ← n - 1
        TANT QUE debut ≤ fin
            milieu ← (debut + fin) // 2
            SI tableau[milieu] == valeur
                retourner VRAI
            SINON SI tableau[milieu] < valeur
                debut ← milieu + 1
            SINON
                fin ← milieu - 1
            FIN SI
        FIN TANT QUE
        retourner FAUX
    FIN
    

Le pseudocode décrit ce processus : on initialise deux indices, debut (0) et fin (n-1), délimitant la partie du tableau à explorer. À chaque itération, on calcule l’indice milieu (moyenne de debut et fin) et compare l’élément à cet indice (`tableau[milieu]`) avec la valeur recherchée. Si les deux sont égaux, l’élément est trouvé (retourner VRAI). Si la valeur est plus grande, la recherche se poursuit dans la moitié droite en ajustant debut à milieu + 1 ; sinon, dans la moitié gauche en ajustant fin à milieu - 1. Le processus se répète tant que debut ≤ fin. Si l’intervalle est épuisé sans trouver la valeur, l’algorithme retourne FAUX, indiquant que l’élément n’est pas dans le tableau.

Pour mieux comprendre l’algorithme, essayez de chercher des nombres dans un tableau trié avec l’application suivante.

 Rechercher

Entrez un nombre et cliquez sur "Rechercher" pour voir les étapes de la recherche binaire.

Observez comment vous faites toujours moins de recherche qu’il y a d’éléments dans le tableau. Pouvez-vous faire en sorte qu’une seule étape soit nécessaire ? Quel est le nombre maximal d’étapes nécessaires ?

Cet algorithme a une complexité en \\( O(\\log n) \\), ce qui le rend très efficace pour les grands tableaux triés. Cela signifie que le nombre d’opérations nécessaires pour trouver (ou ne pas trouver) un élément ne croît pas proportionnellement à la taille du tableau, mais beaucoup plus lentement. Par exemple, pour un tableau de 1 000 000 d’éléments, la recherche binaire nécessite au maximum environ 20 comparaisons (car \\( \\log\_2 1\\,000\\,000 \\approx 20 \\)), alors qu’une recherche linéaire pourrait en demander jusqu’à 1 000 000 dans le pire cas. Plus le tableau est grand, plus l’avantage de la recherche binaire est important.

À chaque étape de la recherche binaire, on divise le nombre d’éléments restants par deux. Si on commence avec \\( n \\) éléments, après une comparaison il en reste \\( n/2 \\), puis \\( n/4 \\), puis \\( n/8 \\), etc. On répète ce processus jusqu’à ce qu’il ne reste qu’un seul élément à examiner.

On cherche donc le nombre d’étapes \\( k \\) tel que :

\\\[ \\frac{n}{2^k} = 1 \\\]

En résolvant pour \\( k \\) :

\\\[ n = 2^k \\implies k = \\log\_2 n \\\]

Ainsi, le nombre maximal de comparaisons est proportionnel à \\( \\log\_2 n \\). C’est pourquoi on dit que la recherche binaire a une complexité en \\( O(\\log n) \\).

---

## pack-m1-11-sorting

**Audit source:** `m1-11-Complexité algorithmique.md`

### Tri

Le tri consiste à réorganiser les éléments d’un tableau ou d’une liste selon un ordre donné (par exemple, croissant). Un algorithme de tri naïf, comme le tri à bulles (bubble sort) ou le tri par insertion, compare chaque élément à tous les autres et échange leur position si nécessaire. Ces algorithmes effectuent environ \\( n^2 \\) comparaisons pour un tableau de taille \\( n \\), ce qui leur donne une complexité en \\( O(n^2) \\). Cela devient très lent dès que le nombre d’éléments augmente.

Pseudocode du tri à bulle:

    POUR i de 0 à n-2
        POUR j de 0 à n-2-i
            SI tableau[j] > tableau[j+1] ALORS
                échanger tableau[j] et tableau[j+1]
            FIN SI
        FIN POUR
    FIN POUR
    

Le tri à bulle est un algorithme de tri simple qui parcourt un tableau de manière répétée pour comparer et échanger les éléments adjacents s’ils sont dans le mauvais ordre. Dans le pseudocode présenté, la boucle externe (i de 0 à n-2) contrôle le nombre de passes sur le tableau, chaque passe garantissant que l’élément le plus grand non encore trié est placé à la fin. La boucle interne (j de 0 à n-2-i) compare chaque paire d’éléments consécutifs (tableau\[j\] et tableau\[j+1\]) et les échange s’ils sont mal ordonnés (tableau\[j\] > tableau\[j+1\]). À chaque itération, les éléments les plus grands “remontent” comme des bulles vers la fin du tableau, d’où le nom de l’algorithme.

Utilisez cette application pour mieux comprendre le tri à bulle.

Lancer le tri Réinitialiser

Un autre algorithme simple est le tri par insertion. Il parcourt le tableau élément par élément, insérant chaque nouvel élément à sa place dans la partie déjà triée.

    POUR i de 1 à n-1
        clé ← tableau[i]
        j ← i - 1
        TANT QUE j ≥ 0 ET tableau[j] > clé
            tableau[j+1] ← tableau[j]
            j ← j - 1
        FIN TANT QUE
        tableau[j+1] ← clé
    FIN POUR
    

Le tri par insertion est un algorithme de tri qui construit progressivement une partie triée du tableau en insérant chaque élément à sa position correcte. Dans le pseudocode fourni, la boucle externe (i de 1 à n-1) sélectionne chaque élément (`clé ← tableau[i]`) à partir du deuxième élément. La boucle interne compare cette clé avec les éléments de la partie déjà triée (de `j ← i-1` jusqu’à 0), en déplaçant les éléments plus grands que la clé d’une position vers la droite (`tableau[j+1] ← tableau[j]`) tant que `tableau[j] > clé` et `j ≥ 0`. Une fois la bonne position trouvée, la clé est insérée (`tableau[j+1] ← clé`). Ce processus répété garantit que, à chaque étape, la sous-partie du tableau jusqu’à l’indice i est triée, aboutissant à un tableau entièrement trié à la fin.

Utilisez cette application pour mieux comprendre le tri par insertion.

Lancer le tri Réinitialiser

Heureusement, il existe des algorithmes de tri plus efficaces. Par exemple, le tri fusion (merge sort) utilise une approche « diviser pour régner » : il divise le tableau en deux moitiés, trie chaque moitié récursivement, puis fusionne les deux moitiés triées en un seul tableau trié. Cette méthode réduit considérablement le nombre de comparaisons nécessaires et atteint une complexité en \\( O(n \\log n) \\).

Idée générale du trie fusion :

1.  Si le tableau contient 0 ou 1 élément, il est déjà trié.
2.  Sinon, on divise le tableau en deux parties de taille à peu près égale.
3.  On trie récursivement chaque partie.
4.  On fusionne les deux parties triées pour obtenir un tableau final trié.

Pseudocode du tri fusion:

    FONCTION triFusion(tableau)
        SI taille(tableau) ≤ 1 ALORS
            retourner tableau
        FIN SI
        milieu ← taille(tableau) // 2
        gauche ← triFusion(tableau[0 .. milieu-1])
        droite ← triFusion(tableau[milieu .. fin])
        retourner fusionner(gauche, droite)
    FIN FONCTION
    
    FONCTION fusionner(gauche, droite)
        résultat ← tableau vide
        TANT QUE gauche et droite ne sont pas vides
            SI gauche[0] ≤ droite[0] ALORS
                ajouter gauche[0] à résultat
                retirer gauche[0] de gauche
            SINON
                ajouter droite[0] à résultat
                retirer droite[0] de droite
            FIN SI
        FIN TANT QUE
        ajouter le reste de gauche (s’il en reste) à résultat
        ajouter le reste de droite (s’il en reste) à résultat
        retourner résultat
    FIN FONCTION
    

Le pseudocode décrit deux fonctions principales. La fonction triFusion divise récursivement le tableau en deux moitiés jusqu’à ce que chaque sous-tableau ait au plus un élément (déjà trié). Pour cela, elle calcule l’indice milieu, trie récursivement la moitié gauche (0 à milieu-1) et la moitié droite (milieu à fin), puis fusionne ces deux sous-tableaux triés. La fonction fusionner combine les sous-tableaux gauche et droite en un tableau trié : elle compare les premiers éléments de chaque sous-tableau, ajoute le plus petit à résultat, et retire cet élément de son sous-tableau d’origine. Ce processus continue jusqu’à ce qu’un des sous-tableaux soit vide, puis les éléments restants de l’autre sous-tableau sont ajoutés à résultat.

Le tri fusion est donc beaucoup plus rapide que les tris naïfs pour les grands tableaux, et il illustre l’intérêt des algorithmes efficaces en informatique.

Utilisez cette application pour mieux comprendre le tri fusion.

Lancer le tri Réinitialiser

Un autre algorithme performant est le tri rapide (quick sort). Il choisit un élément pivot, partitionne le tableau en deux sous-tableaux (les éléments plus petits que le pivot et ceux plus grands), puis trie récursivement chaque sous-tableau. En moyenne, sa complexité est en \\( O(n \\log n) \\), bien qu’il puisse atteindre \\( O(n^2) \\) dans le pire cas (par exemple, si le tableau est déjà trié et que le pivot est mal choisi). Le choix du pivot est crucial : une stratégie courante est de sélectionner la médiane de trois valeurs ou un élément aléatoire.

    FONCTION triRapide(tableau, début, fin)
        SI début < fin ALORS
            pivot ← partitionner(tableau, début, fin)
            triRapide(tableau, début, pivot - 1)
            triRapide(tableau, pivot + 1, fin)
        FIN SI
    FIN FONCTION
    
    FONCTION partitionner(tableau, début, fin)
        pivot ← tableau[fin]
        i ← début - 1
        POUR j de début à fin - 1
            SI tableau[j] ≤ pivot ALORS
                i ← i + 1
                échanger tableau[i] et tableau[j]
            FIN SI
        FIN POUR
        échanger tableau[i + 1] et tableau[fin]
        retourner i + 1
    FIN FONCTION
    

La fonction triRapide vérifie si l’intervalle à trier (de début à fin) contient plus d’un élément ; si oui, elle appelle partitionner pour réorganiser le tableau autour d’un pivot, puis trie récursivement les sous-tableaux à gauche (de début à pivot-1) et à droite (de pivot+1 à fin). La fonction partitionner sélectionne le dernier élément comme pivot (tableau\[fin\]) et réarrange le tableau de sorte que les éléments inférieurs ou égaux au pivot soient à gauche et les plus grands à droite. Elle utilise un indice i pour suivre la frontière des éléments plus petits et échange les éléments appropriés via un parcours (j de début à fin-1). Enfin, le pivot est placé à sa position finale (échange avec tableau\[i+1\]), et son indice (i+1) est retourné.

Utilisez cette application pour mieux comprendre le tri rapide.

Stratégie de pivot : Médiane de troisÉlément aléatoireDernier élémentPremier élément Lancer le tri Réinitialiser

Le tri rapide est souvent le plus rapide en pratique pour plusieurs raisons. Premièrement, le tri rapide est efficace en termes de localité de mémoire. Il travaille directement sur le tableau (tri en place), ce qui minimise les accès mémoire et exploite bien la mémoire tampon des processeurs modernes. Comparé au tri fusion, qui nécessite un tableau auxiliaire pour la fusion, le tri rapide réduit les allocations de mémoire et les copies d’éléments. Deuxièmement, le tri rapide effectue moins de comparaisons en moyenne. Lors du partitionnement, il répartit les éléments autour d’un pivot, ce qui réduit rapidement la taille des sous-tableaux à trier. Si le pivot est bien choisi (par exemple, proche de la médiane), les sous-tableaux sont équilibrés, conduisant à une division efficace du problème. Même avec un choix de pivot aléatoire, les cas défavorables sont rares dans des données réelles. Troisièmement, le tri rapide est adaptable aux données. Dans des ensembles partiellement triés ou avec des motifs courants, il peut tirer parti de ces structures pour réduire le nombre d’échanges. Par exemple, un bon choix de pivot peut minimiser les réarrangements inutiles.

Utilisez l’application suivante pour comparer les techniques de tri. Appuyez sur _Lancer tous les tris_ et regardez les 4 algorithmes s’exécuter en même temps. Constatez que certains algorithmes sont plus rapides que d’autres. Que pensez-vous qu’il se passerait si nous avions moins d’éléments (par ex., 4) ou beaucoup plus d’éléments (par ex., 1000) ?

Lancer tous les tris Réinitialiser Stratégie de pivot (tri rapide) : Médiane de troisÉlément aléatoireDernier élémentPremier élément

Tri à bulles

Tri par insertion

Tri par fusion

Tri rapide

Le Java utilise généralement Timsort. Timsort est un algorithme de tri hybride, conçu par Tim Peters. Il combine le tri par insertion et le tri fusion pour optimiser les performances sur des données réelles, en exploitant les séquences déjà triées, appelées _runs_. L’algorithme commence par diviser le tableau en petits _runs_, soit naturels (séquences croissantes ou décroissantes), soit créés en triant des blocs de taille minimale (souvent 32 éléments) avec le tri par insertion. Ces _runs_ sont ensuite fusionnés deux à deux à l’aide d’une version optimisée du tri fusion, qui minimise les comparaisons et les copies. Sa complexité est en \\( O(n \\log n) \\) dans le pire cas, mais elle peut descendre à \\( O(n) \\) pour des données presque triées, rendant Timsort particulièrement efficace en pratique. De plus, Timsort est stable, préservant l’ordre relatif des éléments égaux, ce qui est crucial dans certaines applications.

Dans certains cas spécialisés, nous utilisons l’algorithme de tri par niches, également connu sous le nom de _pigeonhole sort_, est un algorithme de tri non comparatif adapté aux ensembles de données où les éléments appartiennent à un ensemble fini de valeurs entières, comme des nombres dans une plage limitée. Il repose sur le principe des “niches” (ou pigeonholes) : chaque valeur possible est associée à une niche, et les éléments sont placés dans la niche correspondant à leur valeur. Ensuite, les niches sont parcourues dans l’ordre pour reconstruire le tableau trié. Sa complexité est en \\( O(n + k) \\), où \\( n \\) est le nombre d’éléments et \\( k \\) la taille de la plage de valeurs. Cet algorithme est très efficace lorsque \\( k \\) est proche de \\( n \\), mais il nécessite un espace auxiliaire proportionnel à \\( k \\) et n’est pas adapté aux données non entières ou à des plages de valeurs très grandes.

    FONCTION triParNiches(tableau, min, max)
        k ← max - min + 1  // Taille de la plage de valeurs
        niches ← tableau de taille k, initialisé à vide
    
        // Étape 1 : placer les éléments dans les niches
        POUR chaque élément dans tableau
            index ← élément - min
            ajouter élément à niches[index]
        FIN POUR
    
        // Étape 2 : reconstruire le tableau trié
        index ← 0
        POUR i de 0 à k-1
            TANT QUE niches[i] n’est pas vide
                tableau[index] ← premier élément de niches[i]
                retirer premier élément de niches[i]
                index ← index + 1
            FIN TANT QUE
        FIN POUR
    
        retourner tableau
    FIN FONCTION
    

Le tri par niches (ou bucket sort) est un algorithme de tri non comparatif adapté aux données uniformément réparties dans une plage de valeurs connue (de min à max). Le pseudocode décrit un processus en deux étapes. D’abord, il calcule la taille de la plage (k ← max - min + 1) et crée un tableau niches de taille k, où chaque niche correspond à une valeur possible. Dans l’étape 1, chaque élément du tableau est placé dans la niche correspondante (index ← élément - min), ce qui regroupe les éléments de même valeur. Dans l’étape 2, le tableau est reconstruit en parcourant les niches dans l’ordre (de 0 à k-1) et en extrayant leurs éléments pour les placer séquentiellement dans le tableau (tableau\[index\]). L’indice index suit la position d’insertion.

#### Vidéo suggérée

---

## pack-m1-11-hash-table

**Audit source:** `m1-11-Complexité algorithmique.md`

### Table de hachage

Une table de hachage (ou « hash table ») est une structure de données qui permet d’associer des clés à des valeurs et d’accéder très rapidement à une valeur à partir de sa clé. Le principe repose sur l’utilisation d’une fonction de hachage qui transforme la clé (par exemple, un texte ou un nombre) en un indice de tableau. Les opérations d’insertion, de recherche et de suppression se font en temps moyen \\( O(1) \\), c’est-à-dire en temps constant, quelle que soit la taille de la table (si la fonction de hachage est bonne et la table bien dimensionnée). La table de hachage est efficace pour retrouver rapidement une information à partir d’une clé.

Idée générale :

1.  On applique une fonction de hachage à la clé pour obtenir un indice.
2.  On stocke la valeur à cet indice dans un tableau.
3.  En cas de « collision » (deux clés différentes qui donnent le même indice), on utilise une technique de résolution (chaînage, sondage linéaire, etc.).

Pseudocode d’une recherche dans une table de hachage (sans collision):

    FONCTION rechercher(table, clé)
        indice ← hachage(clé)
        SI table[indice] == clé ALORS
            retourner VRAI
        SINON
            retourner FAUX
        FIN SI
    FIN FONCTION
    

Le pseudocode décrit une fonction de recherche dans une table de hachage, une structure de données optimisée pour retrouver rapidement un élément. La fonction rechercher prend une table (tableau représentant la table de hachage) et une clé à chercher (clé). Elle commence par calculer l’indice correspondant à la clé via une fonction de hachage (indice ← hachage(clé)), qui mappe la clé à une position dans la table. Ensuite, elle vérifie si l’élément à cet indice (`table[indice]`) est égal à la clé recherchée. Si c’est le cas, la fonction retourne VRAI, indiquant que la clé est présente. Sinon, elle retourne FAUX, signifiant que la clé est absente. Ce pseudocode suppose une table de hachage simple sans gestion des collisions (cas où plusieurs clés pointent vers le même indice), ce qui la rend efficace mais limitée aux cas où chaque indice contient au plus un élément.

Pour mieux comprendre, testez l’application suivante. Saisissez des chaînes de caractères qui seront ajoutées à la table de hachage. Pouvez-vous créer une collision ?

 Ajouter

---

## pack-m1-11-same-problem

**Audit source:** `m1-11-Complexité algorithmique.md`

### Un problème résoluble en \\( O(n^2) \\) ou en \\( O(n) \\)

Prenons le problème suivant : « Trouver s’il existe deux éléments dans un tableau qui, additionnés, donnent une valeur cible. »

Solution naïve (\\( O(n^2) \\)) :

    POUR i de 0 à n-1
        POUR j de i+1 à n-1
            SI tableau[i] + tableau[j] == cible
                retourner VRAI
            FIN SI
        FIN POUR
    FIN POUR
    retourner FAUX
    

La boucle externe (POUR i de 0 à n-1) parcourt chaque élément du tableau, tandis que la boucle interne (POUR j de i+1 à n-1) examine tous les éléments suivants (à partir de i+1) pour éviter de considérer le même élément deux fois ou des paires redondantes. À chaque itération, la condition SI `tableau[i] + tableau[j] == cible` teste si la somme des éléments aux indices i et j égale la valeur cible. Si une telle paire est trouvée, la fonction retourne VRAI, indiquant que la solution existe. Si aucune paire ne satisfait la condition après avoir exploré toutes les combinaisons, la fonction retourne FAUX.

Ici, on teste toutes les paires possibles, ce qui prend un temps quadratique.

Solution optimisée (\\( O(n) \\)) :

On peut résoudre ce problème en temps linéaire en utilisant une structure de données comme un ensemble (set) :

    initialiser un ensemble vide
    POUR chaque élément x du tableau
        SI (cible - x) est dans l’ensemble
            retourner VRAI
        AJOUTER x à l’ensemble
    FIN POUR
    retourner FAUX
    

Initialement, un ensemble vide est créé pour stocker les éléments rencontrés. La boucle (POUR chaque élément x du tableau) parcourt chaque élément x du tableau. Pour chaque x, l’algorithme vérifie si cible - x (la valeur nécessaire pour atteindre la somme cible) est déjà dans l’ensemble. Si c’est le cas, une paire d’éléments dont la somme vaut cible a été trouvée, et la fonction retourne VRAI. Sinon, l’élément x est ajouté à l’ensemble pour être utilisé dans les itérations suivantes. Si la boucle se termine sans trouver une telle paire, la fonction retourne FAUX.

Ici, chaque élément est traité une seule fois, et si la recherche dans l’ensemble se fait en temps constant (en moyenne) ou \\( O(1) \\), la solution est en \\( O(n) \\). Dans la solution optimisée, la vérification « (cible - x) est dans l’ensemble » est cruciale. Il n’est pas garanti que la recherche se fasse en temps \\( O(1) \\), mais c’est possible avec une table de hachage.

---

## pack-m1-11-trees

**Audit source:** `m1-11-Complexité algorithmique.md`

### Les arbres en informatique

Les arbres sont des structures de données hiérarchiques non linéaires, composées de nœuds reliés par des arêtes. Un arbre possède une racine unique, à partir de laquelle descendent des sous-arbres. Chaque nœud peut avoir zéro ou plusieurs enfants, mais un seul parent (sauf la racine). À partir du sommet, nous progressons vers les feuilles qui où se terminent la progression. Les arbres permettent de représenter des relations hiérarchiques naturelles, comme des dossiers dans un système de fichiers, des expressions arithmétiques ou des structures organisationnelles.

Parmi les arbres les plus utilisés figure l’arbre binaire, où chaque nœud a au plus deux enfants (gauche et droit). L’arbre binaire de recherche (ABR) est une variante particulièrement utile : pour tout nœud, les valeurs dans le sous-arbre gauche sont inférieures à celle du nœud, et celles dans le sous-arbre droit sont supérieures. Cela permet des opérations de recherche, insertion et suppression efficaces dans un arbre équilibré.

    fonction rechercher(racine, valeur_cible)
        courant ← racine
        tant que courant n'est pas null
            si valeur_cible = courant.valeur
                retourner courant
            fin si
            
            si valeur_cible < courant.valeur
                courant ← courant.gauche
            sinon
                courant ← courant.droit
            fin si
        fin tant que
        
        retourner null  // valeur non trouvée
    fin fonction
    

Pour mieux comprendre le fonctionnement d’un arbre de recherche binaire, utilisez l’application suivante.

 Insérer Rechercher Supprimer Effacer

class Node{constructor(e){this.value=e,this.left=null,this.right=null,this.x=400,this.y=50}}let root=null;const canvas=document.getElementById("canvas"),ctx=canvas.getContext("2d"),nodeRadius=20;let animating=!1;function buildBalanced(e,t,n){if(t>n)return null;let s=Math.floor((t+n)/2),o=new Node(e\[s\]);return o.left=buildBalanced(e,t,s-1),o.right=buildBalanced(e,s+1,n),o}let values=\[10,20,30,40,50,55,70,80\].sort((e,t)=>e-t);root=buildBalanced(values,0,values.length-1);function drawTree(){ctx.clearRect(0,0,canvas.width,canvas.height),root&&drawNode(root,canvas.width/2,50,canvas.width/4)}function drawNode(e,t,n,s){if(!e)return;e.x=t,e.y=n,e.left&&(ctx.beginPath(),ctx.moveTo(t,n),ctx.lineTo(t-s,n+80),ctx.stroke()),e.right&&(ctx.beginPath(),ctx.moveTo(t,n),ctx.lineTo(t+s,n+80),ctx.stroke()),ctx.fillStyle="#f0f0f0",ctx.beginPath(),ctx.arc(t,n,nodeRadius,0,Math.PI\*2),ctx.fill(),ctx.strokeStyle="#000",ctx.stroke(),ctx.fillStyle="#000",ctx.font="14px sans-serif",ctx.textAlign="center",ctx.textBaseline="middle",ctx.fillText(e.value,t,n),drawNode(e.left,t-s,n+80,s/2),drawNode(e.right,t+s,n+80,s/2)}async function insert(e){if(animating)return;if(animating=!0,e=parseInt(e),isNaN(e)){animating=!1;return}if(!root){root=new Node(e),drawTree(),animating=!1;return}let t=root;for(;!0;)if(ctx.fillStyle="rgba(0, 255, 0, 0.3)",ctx.beginPath(),ctx.arc(t.x,t.y,nodeRadius+5,0,Math.PI\*2),ctx.fill(),drawTree(),e<t.value){if(!t.left){t.left=new Node(e),drawTree();break}t=t.left}else if(e>t.value){if(!t.right){t.right=new Node(e),drawTree();break}t=t.right}else break;animating=!1}async function search(e){if(animating||!root)return;animating=!0,e=parseInt(e);let t=root,n=!1;for(;t;){if(drawTree(),ctx.fillStyle="rgba(255, 255, 0, 0.4)",ctx.beginPath(),ctx.arc(t.x,t.y,nodeRadius+5,0,Math.PI\*2),ctx.fill(),await sleep(800),e===t.value){n=!0,ctx.fillStyle="rgba(0, 255, 0, 0.5)",ctx.beginPath(),ctx.arc(t.x,t.y,nodeRadius+5,0,Math.PI\*2),ctx.fill(),await sleep(1e3),drawTree();break}t=e<t.value?t.left:t.right}n||(alert("Valeur non trouvée"),drawTree()),animating=!1}async function remove(e){if(animating||!root)return;animating=!0,root=await removeNode(root,parseInt(e)),drawTree(),animating=!1}async function removeNode(e,t){if(!e)return null;if(ctx.fillStyle="rgba(255, 255, 0, 0.4)",ctx.beginPath(),ctx.arc(e.x,e.y,nodeRadius+5,0,Math.PI\*2),ctx.fill(),drawTree(),t<e.value)e.left=await removeNode(e.left,t);else if(t>e.value)e.right=await removeNode(e.right,t);else{if(ctx.fillStyle="rgba(255, 0, 0, 0.5)",ctx.beginPath(),ctx.arc(e.x,e.y,nodeRadius+5,0,Math.PI\*2),ctx.fill(),drawTree(),!e.left)return e.right;if(!e.right)return e.left;let t=e.right;for(;t.left;)t=t.left;e.value=t.value,e.right=await removeNode(e.right,t.value)}return e}function sleep(e){return new Promise(t=>setTimeout(t,e))}function insertValue(){const e=document.getElementById("value").value;insert(e)}function searchValue(){const e=document.getElementById("value").value;search(e)}function deleteValue(){const e=document.getElementById("value").value;remove(e)}function clearTree(){root=null,drawTree()}drawTree()

Nous souhaitons garder la distance entre le sommet et les feuilles aussi petite que possible. Cette distance détermine notre complexité de recherche. L’arbre rouge-noir (red-black tree) est une des arbres les plus populaires, utilisée notamment dans les implémentations de Map et Set en Java (TreeMap, TreeSet). Chaque nœud est coloré en rouge ou noir, et l’arbre respecte cinq propriétés strictes : la racine est noire, chaque feuille (nil) est noire, un nœud rouge a des enfants noirs, tout chemin d’un nœud à une feuille contient le même nombre de nœuds noirs, et aucun chemin ne contient deux rouges consécutifs. Ces règles assurent que l’arbre reste approximativement équilibré, avec une hauteur maximale d’environ \\( 2 \\log n \\). Lors d’insertions ou suppressions, des violations de couleur peuvent survenir ; elles sont corrigées par des opérations locales qui maintiennent l’équilibre. Les arbres rouge-noir offrent des performances garanties. Les opérations de recherche, insertion et suppression s’exécutent en \\( O(\\log n) \\) dans le pire cas, où \\( n \\) est le nombre de nœuds. Dans ce cours, il n’est pas nécessaire de concevoir des structures en arbres.

#### Vidéo suggérée

---

## pack-m1-11-amortized

**Audit source:** `m1-11-Complexité algorithmique.md`

Analyse amortie
-------------------------------------

L’analyse amortie est une méthode utilisée pour évaluer la complexité moyenne d’une séquence d’opérations sur une structure de données, même si certaines opérations individuelles peuvent être coûteuses. Plutôt que de se concentrer sur le pire cas d’une seule opération, l’analyse amortie considère le coût total de nombreuses opérations et le répartit uniformément, offrant ainsi une vision plus réaliste de la performance globale. Le tri rapide (quick sort) est un algorithme qui a techniquement une complexité \\( O(n^2) \\), mais qui a une complexité amortie de \\( O(n \\log n) \\). En d’autres termes, le tri rapide est généralement rapide, mais il existe des cas rares où il est lent.

---

## pack-m1-12-common-errors

**Audit source:** `m1-12-Les erreurs communes.md`

Erreurs communes
=======================================

Rédiger du pseudo-code n’a rien de sorcier, mais plusieurs étudiants font des erreurs. Voici quelques erreurs communes.

1.  Certains étudiants rédigent du pseudo-code qui a l’air formel et correct, mais qui est en fait ambigu et inutilisable. Prenons cet exemple: `SI j'ai mal aux dos ALORS je prend des aspirines OU SI j'ai faim ALORS je mange`. Bien sûr, je n’ai utilisé que des expressions logiques. Des SI, des ALORS des OU. Mais qu’est-ce que ça signifie ? Par exemple, est-ce que je peux à la fois manger et prendre des aspirines dans ce scénario ? La réponse est subjective. Votre pseudo-code doit être exécutable sans interprétation. Un pseudo-code n’est pas un texte à interprétation subjective. Vous ne pouvez pas faire semblant d’écrire du pseudo-code en utilisant simplement les termes qu’on trouve fréquemment au sein des pseudo-codes. Ce n’est pas une question de syntaxe. On peut parfaitement écrire du pseudo-code sans jamais utiliser SI, TANT QUE, etc. Plusieurs étudiants obsèdent sur la syntaxe, croyant à tort que si on leur donne les bons termes, la bonne grammaire, ils trouveront comment comprendre ce qu’est un pseudo-code. Or, c’est justement le contraire de la leçon ici: nous voulons que vous compreniez que la syntaxe exacte est secondaire dans la pensée algorithmique. On peut être imprécis et incohérent en utilisant une syntaxe formelle, et on peut être précis et cohérent en utilisant du français usuel. Ce n’est pas parce que vous utilisez des expressions qui vous semblent précises que vous l’êtes. Vous devez avoir une idée précise en tête et vous devez l’exprimer avec précision.
    
2.  Au sein d’une boucle (par ex., TANT QUE), les étudiants peuvent mettre par erreur une condition qui termine toujours le programme. Dans un tel cas, la boucle ne peut pas s’exécuter et elle est de facto brisée. Voici un exemple. Les instructions « retourner minimum » et « retourner tableau\[iterateur\] » terminent le pseudo-code. Assurez-vous de bien comprendre que ce pseudo-code ne va consulter que la première valeur du tableau. Si vous avez une condition ou les deux branches (SI et SINON) retournent une valeur et terminent donc l’algorithme, votre algorithme ne procèdera pas plus loin.
    

    Variable iterateur (entier)
    
    Variable minimum  = tableau[0] 
    
    iterateur = 0
    TANT QUE  iterateur < 100  FAIRE
         SI tableau[iterateur] < minimum ALORS
             retourner tableau[iterateur];
         SINON
             retourner minimum
         FIN SI
         iterateur = iterateur + 1;
    FIN TANT QUE
    

3.  Certains étudiants construisent des boucles qui ne se terminent jamais. Dans une boucle TANT QUE, il faut s’assurer que la condition ne soit plus satisfaite pour ne pas avoir une boucle infinie. Consultez cet exemple. Si vous testez votre pseudo-code, vous saurez éviter de telles erreurs.

    iterateur = 0
    TANT QUE  iterateur < 100  FAIRE
         SI iterateur < 10 ALORS
             ajouter un à itérateur
         FIN SI
    FIN TANT QUE
    

4.  Les étudiants vont aussi fréquemment utiliser des variables et des constructions qui ne sont pas définies et dont le sens doit être deviné. Voici un exemple. Vous constaterez à la lecture de ce pseudo-code qu’il y a plusieurs conventions syntaxiques qui ne sont pas définies. Il y a plusieurs variables, mais il est difficile de connaître leur type et leurs relations. Assurez-vous donc de bien expliquer chaque variable et de bien définir votre syntaxe. Dans ce dernier exemple, que représente iterateur, iterateur\[tableau\], tableau\[iterateur\], etc.? Vous devez être précis. Souvent, nous avons un nombre limité de « types » pour les variables: nombres, entiers, chaînes de caractères. On utilise le plus souvent la convention t\[i\] pour désigner l’élément à l’index i du tableau t. Dans un tel cas, t doit être un tableau, i doit être une valeur entière. Vous être libre de concevoir vos propres conventions, mais vous devez être explicite et précis. Si votre pseudo-code doit retourner une valeur, il faut que le pseudo-code le spécifie explicitement.

    Entier iterateur[tableau] = 0;
    TANT QUE  iterateur[i] < 100  FAIRE
         SI tableau[iterateur] < minimum ALORS
             retourner iterateur[tableau];
         FIN SI
         iterateur = iterateur[tableau] + 1;
    FIN POUR TOUT
    

5.  Si vous avez bien défini le type de vos variables, et toutes vos conventions syntaxiques, il vous reste maintenant à vous assurer que les valeurs de vos variables sont toujours spécifiées. Si vous dites que x est un nombre et que vous posez ensuite l’inéquation x > 1, nous ne pouvons en connaître la valeur que si x a reçu une valeur. Assurez-vous donc de donner une valeur initiale à toutes vos variables. En tout temps, dans votre pseudo-code, le lecteur doit pouvoir déterminer la valeur d’une variable donnée.
    
6.  Parfois les étudiants manquent tout simplement de rigueur. Pour vérifiez si votre pseudo-code est rigoureux, appliquez-le sur un exemple concret comme si vous étiez un robot. Par exemple, si quelqu’un écrit le pseudo-code suivant « je prend chacune des valeurs du tableau, et je l’additionne à la valeur suivante dans le tableau »… vous pourriez alors prendre un tableau à titre d’exemple, comme \[1,2,3\] et tester l’instruction. Qu’est-ce que ça donnerait ? Je prend les valeurs une à une et je l’additionne à la valeur suivante dans le tableau. Je prend donc 1 et sa valeur suivante (1 + 2), ensuite 2 et sa valeur suivante (2 + 3), et ensuite 3 et sa valeur suivante… ? Je me rend compte que l’expression « la valeur suivante » n’est pas bien définie. Voici un autre exemple. Quelqu’un pourrait avoir comme pseudo-code « j’initialise la variable comme ayant comme valeur le premier élément du tableau ». Testons ce pseudo-code sur le tableau vide (de taille zéro). Nous constatons qu’il n’y a pas de premier élément ! Donc si le tableau vide n’est pas exclu, nous avons un problème de rigueur. Voici un truc: testez toujours votre pseudo-code avec plusieurs exemples concrets. Prenez le temps d’appliquer les instructions de votre pseudo-code ligne par ligne, comme si vous étiez un robot. Pensez comme un ordinateur!
    

Nous vous invitons maintenant à passez aux premiers exercices du cours!

---

## pack-m1-13-style-guide

**Audit source:** `m1-13-Présentation du pseudocode.md`

Guide pour présenter du pseudocode
================================================================================

Adoptez un style simple. Testez la lisibilité de votre pseudocode en le lisant à haute voix.

Voici un exemple de pseudocode difficile à comprendre.

    entrée : un nombre
    si mon nombre nombre > 0 alors "positif"
         autrement
        afficher "négatif ou zéro"
    fin du code
    

Voici un bon exemple.

    entrée : nombre
    si nombre > 0 alors
        afficher "positif"
    sinon
        afficher "négatif ou zéro"
    fin si
    

Indentation
-----------------------------

L’indentation est utile pour montrer la structure hiérarchique (boucles, conditions, blocs). Utilisez systématiquement 2 à 4 espaces par niveau, vous pouvez aussi utiliser des tabulations. Ne mélangez pas espaces et tabulations. Indentez chaque bloc intérieur d’un niveau supplémentaire. Alignez les instructions de fin de bloc (comme “fin si” ou “fin pour”) avec le début du bloc. Conservez une indentation cohérente dans tout le document.

    pour i de 1 à 10 faire
        si i mod 2 = 0 alors
            afficher i + " est pair"
        fin si
    fin pour
    

Terminologie
-------------------------------

Employez des termes en français ou en anglais courants, mais ne mélangez pas les langues. Utilisez des mots-clés simples et clairs :

*   entrée, sortie
*   si … alors … sinon … fin si
*   pour … faire … fin pour
*   tant que … faire … fin tant que
*   fonction … retour … fin fonction

Évitez les abréviations obscures.

Commentaires
-------------------------------

Insérez des commentaires avec un préfixe comme “//” ou “#” pour expliquer les parties complexes. Numérotez les lignes seulement pour des algorithmes longs ou des références.

Exemple :

    fonction factorielle(n)  // Calcule n!
        si n <= 1 alors
            retour 1
        sinon
            retour n * factorielle(n-1)
        fin si
    fin fonction
    

Typographie
-----------------------------

Utilisez une police à espacement fixe (comme Courier) dans les documents. Évitez les lignes trop longues. Séparez les sections logiques par des lignes vides.

    entrée : nombre
    si nombre > 0 alors
        afficher "positif"
    sinon
        afficher "négatif ou zéro"
    fin si
    
    si nombre > 10 alors
        afficher "nombre plus grand que dix"
    fin si

Indentation
-----------------------------

L’indentation est utile pour montrer la structure hiérarchique (boucles, conditions, blocs). Utilisez systématiquement 2 à 4 espaces par niveau, vous pouvez aussi utiliser des tabulations. Ne mélangez pas espaces et tabulations. Indentez chaque bloc intérieur d’un niveau supplémentaire. Alignez les instructions de fin de bloc (comme “fin si” ou “fin pour”) avec le début du bloc. Conservez une indentation cohérente dans tout le document.

    pour i de 1 à 10 faire
        si i mod 2 = 0 alors
            afficher i + " est pair"
        fin si
    fin pour

Terminologie
-------------------------------

Employez des termes en français ou en anglais courants, mais ne mélangez pas les langues. Utilisez des mots-clés simples et clairs :

*   entrée, sortie
*   si … alors … sinon … fin si
*   pour … faire … fin pour
*   tant que … faire … fin tant que
*   fonction … retour … fin fonction

Évitez les abréviations obscures.

Commentaires
-------------------------------

Insérez des commentaires avec un préfixe comme “//” ou “#” pour expliquer les parties complexes. Numérotez les lignes seulement pour des algorithmes longs ou des références.

Exemple :

    fonction factorielle(n)  // Calcule n!
        si n <= 1 alors
            retour 1
        sinon
            retour n * factorielle(n-1)
        fin si
    fin fonction

Typographie
-----------------------------

Utilisez une police à espacement fixe (comme Courier) dans les documents. Évitez les lignes trop longues. Séparez les sections logiques par des lignes vides.

    entrée : nombre
    si nombre > 0 alors
        afficher "positif"
    sinon
        afficher "négatif ou zéro"
    fin si
    
    si nombre > 10 alors
        afficher "nombre plus grand que dix"
    fin si

---

## pack-m1-14-meta

**Audit source:** `m1-14-Exercices sur les algorithmes.md`

### Réponses uniques ?

Les exercices incluent une solution pour comparer votre approche à la nôtre. Il n’existe pas de solution unique ; votre solution peut être meilleure ou moins bonne que celle proposée.

### Logiciels

Certains étudiants utilisent des logiciels comme [AlgoBox](https://www.xm1math.net/algobox/) ou [PseudoFlow](https://online.pseudoflow.app). Cela n’est pas nécessaire, car le pseudo-code doit être écrit dans vos propres mots. Si un logiciel vous aide, utilisez-le, mais vous devriez pouvoir écrire du pseudo-code manuellement, sans outil. C’est l’essence du pseudo-code : il est indépendant des syntaxes et des outils.

---

## pack-m1-14-ex01

**Audit source:** `m1-14-Exercices sur les algorithmes.md`

### Exercice 1 : La somme d’un tableau

Dans la plupart des langages informatiques, un tableau correspond à un vecteur en algèbre linéaire, soit une série de nombres, comme \\(\\langle 1,6,4,10 \\rangle\\). Dans cet exercice, vous devez proposer un algorithme pour calculer la somme des nombres entiers d’un tableau à une dimension de longueur quelconque (de 0 à plus d’un million de nombres). Utilisez une structure d’itération (boucle) pour parcourir chaque nombre du tableau.

Pour manipuler le tableau, vous pouvez écrire « Récupérer le nombre à l’index i » (où i est une variable contenant l’index) ou utiliser une syntaxe proche des langages de programmation, par exemple : `Entier e = monTableau[i]`. Pour obtenir la longueur du tableau, utilisez « la taille de monTableau ».

Testez votre pseudo-code en l’appliquant ligne par ligne à un exemple, comme si vous étiez un robot. Prenez votre temps.

Si vous introduisez d’autres conventions de notation, soyez précis. Spécifiez le type de toutes vos variables et donnez explicitement des valeurs initiales, sauf si elles sont reçues en paramètre.

Concevez cet algorithme en pseudo-code, en utilisant des termes concis, explicatifs et cohérents.

Réponse

    Entrée :
    Tableau d’entiers monTableau de taille N
    
    Variables :
    Entier somme = 0 // La somme du tableau
    Entier index = 0 // Index de l’élément du tableau
    
    Sortie :
    Entier somme
    
    Algorithme sommeTableau :
    
    TANT QUE index < taille de monTableau FAIRE
        somme = somme + monTableau[index] // Addition des nombres
        index = index + 1 // Incrémentation de l’index
    FIN TANT QUE
    
    retourne somme

---

## pack-m1-14-ex02

**Audit source:** `m1-14-Exercices sur les algorithmes.md`

### Exercice 2 : La recherche d’un entier

La recherche d’information dans une structure de données (tableau, graphe, arbre, etc.) est un domaine clé en informatique. Bien que les bases de données comme MySQL simplifient la recherche, il est souvent nécessaire de concevoir ses propres solutions. À partir de l’exercice 1, proposez un algorithme en pseudo-code pour vérifier si un entier (par exemple, un numéro de téléphone) est présent dans un tableau et retourner son index, ou -1 s’il est absent. Utilisez une structure itérative et une structure de contrôle (SI \_ ALORS \_ FIN SI).

Réponse

    Entrée :
    Tableau d’entiers monTableau de taille N
    Entier nombreATrouver
    
    Variables :
    Entier index = 0 // Index de l’élément du tableau
    
    Sortie :
    Index de l’entier ou -1 si non trouvé
    
    Algorithme trouverEntier :
    
    TANT QUE index < taille de monTableau FAIRE
        SI nombreATrouver est égal à monTableau[index] ALORS
            retourner index // Fin de l’algorithme
        FIN SI
        index = index + 1 // Incrémentation de l’index
    FIN TANT QUE
    
    retourner -1 // Nombre non trouvé

---

## pack-m1-14-ex03

**Audit source:** `m1-14-Exercices sur les algorithmes.md`

### Exercice 3 : Somme des multiples de 3 ou 5

Additionnez tous les nombres naturels inférieurs à \\(1000\\) qui sont multiples de \\(3\\) ou de \\(5\\).

Réponse

Voici un algorithme inefficace. Vous pouvez faire mieux :

    Variable entière i = 0
    Variable entière somme = 0
    TANT QUE i < 1000
        SI le reste de la division par 3 de i est zéro OU le reste de la division par 5 de i est zéro ALORS
            somme = somme + i
        i = i + 1
    FIN TANT QUE
    Retourne somme

---

## pack-m1-14-ex04

**Audit source:** `m1-14-Exercices sur les algorithmes.md`

### Exercice 4 : Plus grand diviseur premier

Trouvez le plus grand nombre premier qui divise \\(317584931803\\).

Réponse

Voici un algorithme inefficace (effectuant plus d’opérations que nécessaire). Vous pouvez faire mieux :

    Variable entière i = 1
    Variable entière solution = 1
    TANT QUE i < 317584931803
        SI le reste de la division de 317584931803 par i est zéro ALORS
            Variable entière j = 3
            Variable booléenne premier = vrai
            TANT QUE j < i
                SI le reste de la division de i par j est zéro ALORS
                    premier = faux
                j = j + 1
            FIN TANT QUE
            SI premier ALORS
                solution = i
        i = i + 1
    FIN TANT QUE
    Retourne solution
    

Pour les curieux, voici une solution exécutable en Python ([voir ici](https://fr.wikipedia.org/wiki/Python_%28langage%29)) :

    i = 1
    solution = 1
    while i < 317584931803:
        if 317584931803 % i == 0:
            j = 3
            premier = True
            while j < i:
                if i % j == 0:
                    premier = False
                j = j + 1
            if premier:
                print(i, " est premier")
                solution = i
        i = i + 1
    print(solution)
    

Vous pouvez supprimer la ligne `print(i, " est premier")` pour n’obtenir que la réponse finale. Notez que j commence à 3, car tout diviseur premier (sauf 2) est impair d’après le théorème fondamental de l’arithmétique.

---

## pack-m1-14-ex05

**Audit source:** `m1-14-Exercices sur les algorithmes.md`

### Exercice 5 : Chiffre des dizaines

Pour un entier positif \\(x\\), trouvez le chiffre occupant la position des dizaines.

Réponse

    Variable entière x
    
    Divise x par 10, stocke le quotient dans la variable y
    
    Divise y par 10, retourne le reste de la division
    

Exemple : si x est 531, le quotient de 531 divisé par 10 est 53, reste 1. Le quotient de 53 divisé par 10 est 5, reste 3.

---

## pack-m1-14-ex06

**Audit source:** `m1-14-Exercices sur les algorithmes.md`

### Exercice 6 : Erreur dans un pseudo-code

Trouvez l’erreur dans le pseudo-code suivant :

    Entrées :
    Tableau R de longueur N
    Valeur X
    
    Sortie :
    Est-ce que la valeur X se trouve dans le tableau R ?
    
    Variables :
    Itérateur i = 0
    
    Tant que i <= N
        Si R[i] = X Alors retourne Vrai
        i = i + 1
    
    retourne Faux
    

Réponse

L’itérateur i prend les valeurs de 0 à N, accédant ainsi à N+1 éléments du tableau R, ce qui provoque une erreur d’accès hors limites.

---

## pack-m1-14-ex07

**Audit source:** `m1-14-Exercices sur les algorithmes.md`

### Exercice 7 : Racines d’un polynôme du second degré

Soit \\(P(x) = ax^2 + bx + c\\) un polynôme du second degré à coefficients réels. Les racines se calculent via le discriminant \\(A = b^2 - 4ac\\).

*   Si \\(A < 0\\), il n’y a pas de racine.
*   Si \\(A > 0\\), il existe deux racines : \\(X\_1 = \\frac{-b - \\sqrt{A}}{2a}\\) et \\(X\_2 = \\frac{-b + \\sqrt{A}}{2a}\\).
*   Si \\(A = 0\\), il existe une racine double : \\(X\_1 = X\_2 = \\frac{-b}{2a}\\).

Écrivez un algorithme qui, pour un polynôme donné par ses coefficients, calcule le discriminant, affiche « ce polynôme n’a pas de racine dans R » si A < 0, et calcule les racines sinon.

Réponse

    Algo pol
    
    Entrée :
    Nombres réels a, b, c // Coefficients du polynôme
    
    Variables :
    Nombres réels X1, X2, A // Racines et discriminant
    
    Début
        A = b² - 4ac
        Si A < 0 Alors
            Afficher «&nbsp;ce polynôme n’a pas de racine dans R&nbsp;»
        Sinon
            Si A égale 0
                X1 = X2 = -b/(2a)
            Sinon // A > 0
                X1 = (-b - √A)/(2a)
                X2 = (-b + √A)/(2a)
            Fin Si
        Fin Si
    Fin

---

## pack-m1-14-ex08

**Audit source:** `m1-14-Exercices sur les algorithmes.md`

### Exercice 8 : Exécution de l’algorithme des racines

Exécutez l’algorithme de l’exercice 7 pour \\(P(x) = x^2 - 5x + 6\\), en présentant les résultats dans un tableau.

Réponse

Initialisation

Étape 1

Étape 2

Étape 3

Fin

Entrée

a

1

1

1

1

1

b

\-5

\-5

\-5

\-5

\-5

c

6

6

6

6

6

Variables

X1

2

2

2

X2

3

3

A

1

1

1

1

Sorties

écran

---

## pack-m1-14-ex09

**Audit source:** `m1-14-Exercices sur les algorithmes.md`

### Exercice 9 : Conversion de base

Pour un entier \\(B > 1\\) et un nombre \\(M\\), la représentation en base \\(B\\) de \\(M\\) s’obtient par division successive : \\(M = B \\times Q\_1 + R\_1\\), puis \\(Q\_1 = B \\times Q\_2 + R\_2\\), jusqu’à un quotient inférieur à \\(B\\). La représentation est \\(Q\_{n-1}R\_n\\ldots R\_1\\). Si \\(B > 10\\), les chiffres de \\(10\\) à \\(B-1\\) sont notés \\(A, B, C, \\ldots\\) (par exemple, pour \\(B = 16\\), \\(10 = A\\), \\(11 = B\\), etc.).

Écrivez un algorithme pour convertir un nombre \\(M\\) dans une base \\(B ≥ 2\\) (\\(B < 17\\)). Affichez un message d’erreur si \\(B < 2\\).

Réponse

    Algo base
    
    Entrée :
    Nombre entier positif B // Base
    Nombre entier positif M // Nombre à convertir
    
    Variables :
    Nombre entier q, r
    Suite de caractères alphanumériques S
    
    Début
        S = chaîne vide
        Si B < 2 Alors
            Afficher «&nbsp;entrez un entier supérieur ou égal à 2&nbsp;»
        Sinon
            q = M
            Tant que q > 0
                r = q - (q ÷ B) × B
                au cas où r
                    égal à 10 : ajouter A au début de S
                    égal à 11 : ajouter B au début de S
                    égal à 12 : ajouter C au début de S
                    égal à 13 : ajouter D au début de S
                    égal à 14 : ajouter E au début de S
                    égal à 15 : ajouter F au début de S
                    dans tous les autres cas : ajouter r au début de S
                q = q ÷ B
            Fin Tant que
        Fin Si
    Fin
    

Voici l’équivalent en Python ([voir ici](https://www.python.org)) :

    def f(M, B):
        s = ""
        if B < 2:
            print("entrez un entier supérieur ou égal à 2")
            return
        q = M
        while q > 0:
            r = q - (q // B) * B
            if r == 10: s = "A" + s
            elif r == 11: s = "B" + s
            elif r == 12: s = "C" + s
            elif r == 13: s = "D" + s
            elif r == 14: s = "E" + s
            elif r == 15: s = "F" + s
            else: s = str(r) + s
            q = q // B
        return s

---

## pack-m1-14-ex10

**Audit source:** `m1-14-Exercices sur les algorithmes.md`

### Exercice 10 : Tester la parité en base 2

En utilisant l’algorithme Algo\_base, qui retourne la représentation en base \\(B\\) d’un nombre \\(M\\) (\\(S = \\text{Algo\\\_base}(B, M)\\)), écrivez un algorithme qui teste la parité d’un nombre \\(M\\) et affiche « pair » ou « impair ».

Réponse

    Algo parité
    
    Entrée :
    Nombre entier positif M // Nombre à tester
    
    Variables :
    Suite de caractères alphanumériques S
    
    Début
        S = Algo_base(2, M)
        Si dernier caractère de S est égal au chiffre 0 Alors
            Afficher «&nbsp;pair&nbsp;»
        Sinon
            Afficher «&nbsp;impair&nbsp;»
        Fin Si
    Fin

---

## pack-m1-14-ex11

**Audit source:** `m1-14-Exercices sur les algorithmes.md`

### Exercice 11 : Calcul de la factorielle

Écrivez un algorithme qui calcule la factorielle d’un entier positif \\(n\\) (\\(n!\\)).

Solution

    Entrée :
    Entier positif n
    
    Variable :
    Entier fact = 1
    Entier i = 1
    
    TANT QUE i <= n FAIRE
        fact = fact × i
        i = i + 1
    FIN TANT QUE
    
    Retourner fact

---

## pack-m1-14-ex12

**Audit source:** `m1-14-Exercices sur les algorithmes.md`

### Exercice 12 : Inverser un tableau

Proposez un algorithme pour inverser un tableau d’entiers de taille quelconque.

Solution

    Entrée :
    Tableau d’entiers T de taille N
    
    Variables :
    Entier i = 0
    Entier j = N - 1
    
    TANT QUE i < j FAIRE
        échanger T[i] et T[j]
        i = i + 1
        j = j - 1
    FIN TANT QUE
    
    Retourner T

---

## pack-m1-14-ex13

**Audit source:** `m1-14-Exercices sur les algorithmes.md`

### Exercice 13 : Compter les voyelles

Écrivez un algorithme qui compte le nombre de voyelles dans une chaîne de caractères donnée.

Solution

    Entrée :
    Chaîne de caractères S
    
    Variable :
    Entier compteur = 0
    Entier i = 0
    
    TANT QUE i < longueur de S FAIRE
        SI S[i] est une voyelle ALORS
            compteur = compteur + 1
        FIN SI
        i = i + 1
    FIN TANT QUE
    
    Retourner compteur

---

## pack-m1-14-ex14

**Audit source:** `m1-14-Exercices sur les algorithmes.md`

### Exercice 14 : Tester si un entier est un palindrome

Donnez un algorithme pour déterminer si un nombre entier est un palindrome (se lit de la même façon de gauche à droite et de droite à gauche).

Solution

    Entrée :
    Entier positif n
    
    Variables :
    Entier original = n
    Entier renverse = 0
    
    TANT QUE n > 0 FAIRE
        renverse = renverse × 10 + (reste de la division de n avec 10)
        n = n ÷ 10
    FIN TANT QUE
    
    SI original = renverse ALORS
        Retourner Vrai
    SINON
        Retourner Faux
    FIN SI

---

## pack-m1-14-ex15

**Audit source:** `m1-14-Exercices sur les algorithmes.md`

### Exercice 15 : Minimum et maximum d’un tableau

Écrivez un algorithme qui trouve le minimum et le maximum dans un tableau d’entiers.

Solution

    Entrée :
    Tableau d’entiers T de taille N
    
    Variables :
    Entier min = T[0]
    Entier max = T[0]
    Entier i = 1
    
    TANT QUE i < N FAIRE
        SI T[i] < min ALORS
            min = T[i]
        FIN SI
        SI T[i] > max ALORS
            max = T[i]
        FIN SI
        i = i + 1
    FIN TANT QUE
    
    Retourner min, max

---

## pack-m1-14-ex16

**Audit source:** `m1-14-Exercices sur les algorithmes.md`

### Exercice 16 : Recherche dans un tableau

Quel est le nombre maximal de comparaisons nécessaires pour rechercher un élément dans un tableau non trié de taille \\( n \\) ? Justifiez votre réponse.

Solution

Dans un tableau non trié de taille \\( n \\), il faut au pire comparer l’élément recherché à chaque élément du tableau, soit \\( n \\) comparaisons. Cela correspond à une recherche linéaire, de complexité \\( O(n) \\).

---

## pack-m1-14-ex17

**Audit source:** `m1-14-Exercices sur les algorithmes.md`

### Exercice 17 : Recherche binaire

Pourquoi la recherche binaire n’est-elle applicable qu’aux tableaux triés ? Quelle est sa complexité en temps ?

Solution

La recherche binaire n’est applicable qu’aux tableaux triés, car elle repose sur le fait que l’on peut éliminer la moitié des éléments à chaque étape en comparant la valeur recherchée à l’élément du milieu. Si le tableau n’est pas trié, on ne peut pas savoir dans quelle moitié chercher. Sa complexité en temps est \\( O(\\log n) \\).

---

## pack-m1-14-ex18

**Audit source:** `m1-14-Exercices sur les algorithmes.md`

### Exercice 18 : Algorithme quadratique

Donnez un exemple d’algorithme ayant une complexité en \\( O(n^2) \\) et expliquez pourquoi.

Solution

Un exemple classique est le tri à bulles (bubble sort). Pour chaque élément, on compare avec tous les autres, ce qui fait environ \\( n^2 \\) comparaisons pour un tableau de taille \\( n \\). C’est pourquoi sa complexité est \\( O(n^2) \\).

---

## pack-m1-14-ex19

**Audit source:** `m1-14-Exercices sur les algorithmes.md`

### Exercice 19 : Algorithme de tri efficace

Un algorithme de tri efficace comme le tri fusion (merge sort) a une complexité en \\( O(n \\log n) \\). Expliquez ce que cela signifie et pourquoi c’est plus rapide qu’un tri naïf pour de grands tableaux.

Solution

Une complexité en \\( O(n \\log n) \\) signifie que le nombre d’opérations croît plus vite que linéairement, mais beaucoup moins vite que quadratiquement. Par exemple, le tri fusion (merge sort) divise le tableau en deux à chaque étape (logarithmique) et traite chaque élément à chaque niveau de division (linéaire), d’où le \\( n \\log n \\). Pour de grands tableaux, c’est beaucoup plus rapide qu’un tri naïf en \\( O(n^2) \\).

---

## pack-m1-14-ex20

**Audit source:** `m1-14-Exercices sur les algorithmes.md`

### Exercice 20 : Alan Kay

Alan Kay est considéré comme l’un des pères de la programmation orientée objet. Quelles étaient ses motivations principales lorsqu’il a conçu ce paradigme ? En quoi sa vision différait-elle de l’utilisation courante de la programmation orientée objet aujourd’hui ? Résumez brièvement ses objectifs et l’esprit original de la programmation orientée objet selon Kay.

Réponse

Alan Kay a conçu la programmation orientée objet pour faciliter la création de systèmes logiciels modulaires, flexibles et évolutifs, inspirés par la biologie et la communication entre objets autonomes. Son objectif principal était de permettre à chaque « objet » d’être responsable de son propre état et de communiquer avec d’autres objets uniquement via des messages, favorisant ainsi l’encapsulation et l’indépendance des composants.

Pour Kay, la programmation orientée objet devait avant tout encourager l’émergence de systèmes dynamiques, adaptatifs et faciles à modifier, plutôt que de se limiter à la simple hiérarchie de classes et à l’héritage. Il insistait sur l’importance de la communication par messages et sur la capacité à faire évoluer les programmes sans tout réécrire.

De nos jours, la programmation orientée objet est souvent réduite à l’organisation du code et des données, alors que la vision originale de Kay mettait l’accent sur la modularité, la flexibilité et l’autonomie des objets. Sa conception visait à rendre la programmation plus naturelle, intuitive et proche du fonctionnement des systèmes vivants.

---

## pack-m1-14-ex21

**Audit source:** `m1-14-Exercices sur les algorithmes.md`

### Exercice 21 : Dahl et Nygaard

Ole-Johan Dahl et Kristen Nygaard sont les créateurs du premier langage orienté objet, Simula. Quelles étaient leurs motivations principales lors de la création de ce langage ? Expliquez en quoi leur approche a influencé la programmation moderne.

Réponse

Dahl et Nygaard ont conçu Simula pour faciliter la modélisation et la simulation de systèmes complexes, comme des réseaux, des usines ou des processus sociaux. Leur motivation était de représenter chaque entité du système par un « objet » autonome, regroupant données et comportements, afin de refléter la réalité de manière plus naturelle et modulaire.

Ils voulaient permettre l’encapsulation, la réutilisation du code grâce à l’héritage, et la création de structures hiérarchiques. Cette approche a posé les bases de la programmation orientée objet moderne, en rendant la conception de logiciels plus flexible, évolutive et adaptée à la complexité des systèmes réels.

---

## pack-m1-14-ex22

**Audit source:** `m1-14-Exercices sur les algorithmes.md`

### Exercice 22 : James Gosling

Qui est James Gosling et quel a été son rôle dans la création du langage Java ? Quelles étaient les motivations principales derrière la conception de Java ?

Réponse

James Gosling est un informaticien canadien considéré comme le principal créateur du langage Java, développé chez Sun Microsystems dans les années 1990. Son objectif était de concevoir un langage portable, sécurisé, simple et adapté aux systèmes embarqués et aux réseaux. Java devait permettre d’écrire un programme une seule fois et de l’exécuter partout (« Write Once, Run Anywhere »), grâce à la machine virtuelle Java (JVM).

---

## pack-m1-14-ex23

**Audit source:** `m1-14-Exercices sur les algorithmes.md`

### Exercice 23 : domaines industriels

Citez trois domaines ou secteurs industriels où Java est largement utilisé aujourd’hui. Expliquez brièvement pourquoi Java est apprécié dans ces contextes.

Réponse

Java est largement utilisé dans :

*   **Le développement d’applications d’entreprise** (banques, assurances, télécommunications), grâce à sa robustesse, sa sécurité et la richesse de ses bibliothèques.
*   **Le développement d’applications mobiles** (notamment Android), car Java est le langage principal pour Android et bénéficie d’un vaste écosystème.
*   **Les systèmes embarqués et l’Internet des objets (IoT)**, où la portabilité et la fiabilité de Java sont des atouts majeurs.

---

## pack-m1-14-ex24

**Audit source:** `m1-14-Exercices sur les algorithmes.md`

### Exercice 24 : Backus-Naur

Qu’est-ce que la notation de Backus-Naur (BNF) ? À quoi sert-elle en informatique ? Donnez un exemple simple de BNF décrivant la syntaxe d’une expression arithmétique composée de chiffres et de l’opérateur +.

Réponse

La notation de Backus-Naur (BNF) est une méthode formelle pour décrire la syntaxe des langages de programmation et des langages formels. Elle permet de spécifier les règles de formation des expressions valides dans un langage, en utilisant des symboles non terminaux, des symboles terminaux et des règles de production.

La BNF est largement utilisée pour définir la grammaire des langages de programmation, des protocoles ou des formats de données.

**Exemple de BNF pour une expression arithmétique simple :**

<expression> ::= <chiffre> | <expression> "+" <chiffre>
<chiffre> ::= "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9"

Cela décrit une expression composée d’un ou plusieurs chiffres séparés par des +.

---

## pack-m1-14-ex25

**Audit source:** `m1-14-Exercices sur les algorithmes.md`

### Exercice 25 : Cycles

Mon ordinateur roule à une fréquence de 3 GHz. À tous les cycles, il exécute ses opérations. Quelle distance est-ce que la vitesse de la lumière traverse pendant un cycle ?

Réponse

À 3 GHz, un cycle d’horloge dure :

1 / 3 000 000 000 = 0,333... nanoseconde (ns) par cycle.

La lumière parcourt environ 30 cm (0,3 mètre) en 1 ns. Donc, en 0,333 ns, elle parcourt :

30 cm × 0,333... ≈ 10 cm.

**Réponse :** Pendant un cycle d’horloge à 3 GHz, la lumière parcourt environ 10 centimètres dans le vide.

---

## pack-m1-14-ex26

**Audit source:** `m1-14-Exercices sur les algorithmes.md`

### Exercice 26 : kibioctet

Quelle est la différence entre un kibioctet et un kilo-octet ?

Réponse

Un kilo-octet (ko) correspond à 1 000 octets (selon le système décimal, préfixe SI), tandis qu’un kibioctet (Kio) correspond à 1 024 octets (selon le système binaire, préfixe IEC). Le préfixe « kilo » (k) est utilisé pour les puissances de 10, alors que « kibi » (Ki) est utilisé pour les puissances de 2. Ainsi, 1 Kio = 1 024 octets, 1 ko = 1 000 octets.

---

## pack-m1-14-ex27

**Audit source:** `m1-14-Exercices sur les algorithmes.md`

### Exercice 27 : doublons

Écrivez un algorithme qui supprime les doublons d’un tableau d’entiers trié en ordre croissant, en renvoyant la nouvelle taille du tableau.

Réponse

    Entrée :
    Tableau d’entiers trié T de taille N
    
    Variables :
    Entier nouvelle_taille = 1
    Entier i = 1
    
    Tant que i < N faire
        Si T[i] ≠ T[nouvelle_taille - 1] alors
            T[nouvelle_taille] = T[i]
            nouvelle_taille = nouvelle_taille + 1
        Fin si
        i = i + 1
    Fin tant que
    
    Retourner nouvelle_taille

---

## pack-m1-14-ex28

**Audit source:** `m1-14-Exercices sur les algorithmes.md`

### Exercice 28 : puissance

Écrivez un algorithme qui calcule \\( a^n \\), où \\( a \\) est un entier et \\( n \\) un entier positif.

Réponse

    
    Entrée :
    Entier a
    Entier positif ou nul n
    
    Variable :
    Entier résultat = 1
    Entier i = 0
    
    Tant que i < n faire
        résultat = résultat × a
        i = i + 1
    Fin tant que
    
    Retourner résultat

---

## pack-m1-14-ex29

**Audit source:** `m1-14-Exercices sur les algorithmes.md`

### Exercice 29 : occurrences d’un caractère spécifique

Écrivez un algorithme qui compte le nombre d’occurrences d’un caractère spécifique dans une chaîne de caractères.

Réponse

    Entrée :
    Chaîne de caractères S
    Caractère c
    
    Variable :
    Entier compteur = 0
    Entier i = 0
    
    Tant que i < longueur de S faire
        Si S[i] = c alors
            compteur = compteur + 1
        Fin si
        i = i + 1
    Fin tant que
    
    Retourner compteur

---

## pack-m1-14-ex30

**Audit source:** `m1-14-Exercices sur les algorithmes.md`

### Exercice 30 : recherche d’une clé

Quelle est la complexité algorithme de la recherche d’un clé dans une table de hachage ?

Réponse

Un temps moyen de \\( O(1) \\).

### Vidéos suggérées

Des vidéos sur l’algorithmique et le pseudo-code sont disponibles, comme [celles de Loïc & Julien](https://www.youtube.com/playlist?list=PLdi5YpL19uBDkRVGWMeZ0ZhtUQKOW-hUZ).

*   *   [Réponses uniques ?](#réponses-uniques-)

---
