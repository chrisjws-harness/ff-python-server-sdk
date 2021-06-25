from featureflags.evaluation.clause import Clause, Clauses
from featureflags.evaluation.constants import (
    CONTAINS_OPERATOR,
    ENDS_WITH_OPERATOR,
    EQUAL_OPERATOR,
    EQUAL_SENSITIVE_OPERATOR,
    GT_OPERATOR,
    IN_OPERATOR,
    SEGMENT_MATCH_OPERATOR,
    STARTS_WITH_OPERATOR,
)
from featureflags.evaluation.target import Target


def test_evaluate_clauses():
    target = Target(
        identifier="john", anonymous=False, attributes={"email": "john@doe.com"}
    )
    clause_1 = Clause(
        attribute="email",
        id="",
        negate=False,
        op=EQUAL_OPERATOR,
        value=["john@doe.com"],
    )
    clause_2 = Clause(
        attribute="anonymous", id="", negate=False, op=EQUAL_OPERATOR, value=[False]
    )
    clauses = Clauses([clause_1, clause_2])

    got = clauses.evaluate(target, [])

    assert got == True