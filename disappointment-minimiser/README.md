# Team 6: Disappointment Minimiser

The program is designed to assign teams to projects according to teams' preferences. It avoids assigning teams their least preferred choice as much as possible, rather than giving as many people their first choice as possible.

## To use
Replace `code-olympics-selections.txt` with similarly formatted table of teams and picks.
Run with Python.

## Output
Each row shows one project and the teams allocated to that project. The disappointment quantifier is shown underneath the project rows.

## Design
- Assign all groups to all projects. 
- Remove teams from their least preferred projects until a project has reached the minimum number of teams assigned.
- If there are any duplicates, remove teams (with least preference) from the largest group until there are no more duplicates.

## Disappointment quantifier
Getting a 1st pick is ideal, but a 2nd pick wouldn't be too bad either. A third pick would be rather disappointing, and not getting any of your choices would be terrible. Therefore the formula for weighting to quantify a team's disappointment is:

`disappointment = 3**(pick-1) - 1`

For three picks out of four choices, the disappointment from 1st to 4th pick would be:

`0, 2, 8, 26`

The total disappointment is the sum of disappointment values from each team.

 
