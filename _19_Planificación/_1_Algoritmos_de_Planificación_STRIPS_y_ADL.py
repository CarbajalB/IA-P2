from PDDL import PDDL_Parser
from PDDL import PDDL_Planner

# Definir el dominio ADL
adl_domain = """
(define (domain adl-blocksworld)
  (:requirements :adl)
  (:predicates (clear ?x)
              (on ?x ?y)
              (holding ?x)
              (handempty))
  (:action pick-up
   :parameters (?x)
   :precondition (and (clear ?x) (handempty))
   :effect (and (holding ?x) (not (clear ?x)) (not (handempty))))
  (:action put-down
   :parameters (?x)
   :precondition (holding ?x)
   :effect (and (clear ?x) (handempty) (not (holding ?x)))
)
"""

# Definir el problema ADL
adl_problem = """
(define (problem prob2)
  (:domain adl-blocksworld)
  (:objects a)
  (:init (clear a) (handempty))
  (:goal (and (clear a) (handempty)))
)
"""

# Crear objetos de análisis PDDL
adl_parser = PDDL_Parser()
adl_parser.parse_domain(adl_domain)
adl_parser.parse_problem(adl_problem)

# Resolver el problema ADL usando Fast Downward
adl_planner = PDDL_Planner(adl_parser)
adl_solution = adl_planner.find_plan()

if adl_solution is not None:
    print("Plan encontrado:")
    for step in adl_solution:
        print(step)
else:
    print("No se pudo encontrar un plan.")
