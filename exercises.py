"""
PYTHON GYM — Python Programming Refresher

Goal:
    Implement every TODO until:

        python python_gym.py

    prints:

        ALL EXERCISES PASSED

Suggested approach:
    1. Do not use AI/autocomplete initially.
    2. Run this file frequently.
    3. Read the failing assertion.
    4. Implement the smallest correct solution.
    5. Refactor once green.

Topics:
    - Lists, dicts, sets, tuples
    - Comprehensions
    - enumerate / zip
    - unpacking
    - sorting
    - functions
    - *args / **kwargs
    - closures
    - iterators / generators
    - dataclasses
    - classes
    - properties
    - classmethod / staticmethod
    - inheritance
    - ABC
    - typing
    - TypeVar / Generic
    - Protocol
    - TypedDict
    - Literal
    - Callable
    - overload
    - context managers
    - decorators
    - exceptions
    - async / await
    - gather
    - create_task
    - as_completed
    - Semaphore
    - async iterators
    - async context managers
    - cancellation
"""

from __future__ import annotations

import asyncio
import time

from abc import ABC, abstractmethod
from collections.abc import (
    AsyncIterator,
    Callable,
    Generator,
    Iterable,
    Iterator,
)
from contextlib import asynccontextmanager, contextmanager
from dataclasses import dataclass
from functools import wraps
from typing import (
    ClassVar,
    Generic,
    Literal,
    Protocol,
    Self,
    TypeVar,
    TypedDict,
    cast,
    overload,
)


# ============================================================
# SECTION 1 — COLLECTIONS
# ============================================================


# Exercise 1
def even_numbers(numbers: list[int]) -> list[int]:
    """Return only even numbers."""
    even = [i for i in numbers if i % 2 == 0]
    return even 


# Exercise 2
def unique_words(words: list[str]) -> set[str]:
    """Return unique lowercase words."""
    return set(word.lower() for word in words)


# Exercise 3
def word_lengths(words: list[str]) -> dict[str, int]:
    """Map each word to its length."""
    return {word: len(word) for word in words}
    


# Exercise 4
def swap(pair: tuple[str, int]) -> tuple[int, str]:
    """Swap the two tuple values."""
    #return (pair[1], pair[0])
    #return tuple(reversed(pair))
    #a,b = pair
    #return b,a
    return pair[::-1]


## TODO - refresh regarding array manipulation


# ============================================================
# SECTION 2 — COMPREHENSIONS
# ============================================================


# Exercise 5
def squares(numbers: Iterable[int]) -> list[int]:
    """Return squares using a list comprehension."""
    return [x*x for x in numbers]


# Exercise 6
def active_usernames(users: list[dict[str, object]]) -> list[str]:
    """
    Return lowercase names of active users.

    Example:
        [
            {"name": "Alice", "active": True},
            {"name": "Bob", "active": False},
        ]

        -> ["alice"]
    """
    return [user['name'].lower() for user in users if user['active']]

# Exercise 7
def invert(mapping: dict[str, int]) -> dict[int, str]:
    """Invert keys and values using a dict comprehension."""
    # return {b:a for a,b in mapping.items()}
    return dict(zip(mapping.values(), mapping.keys()))

    ## TODO - remember .values(), .keys() and .items()


# ============================================================
# SECTION 3 — ENUMERATE / ZIP
# ============================================================


# Exercise 8
def numbered(items: Iterable[str]) -> list[tuple[int, str]]:
    """
    Return:
        [(1, "a"), (2, "b"), ...]
    """
    return [(i,a) for i,a in enumerate(items, start=1)]


# Exercise 9
def combine(
    names: Iterable[str],
    scores: Iterable[int],
) -> list[tuple[str, int]]:
    """Combine names and scores."""
    # TODO: zip
    raise NotImplementedError


# Exercise 10
def score_dictionary(
    names: Iterable[str],
    scores: Iterable[int],
) -> dict[str, int]:
    """Combine two iterables into a dictionary."""
    # TODO
    raise NotImplementedError


# ============================================================
# SECTION 4 — UNPACKING
# ============================================================


# Exercise 11
def first_middle_last(
    values: list[int],
) -> tuple[int, list[int], int]:
    """
    [1, 2, 3, 4, 5] -> (1, [2,3,4], 5)

    Use starred unpacking.
    """
    # TODO
    raise NotImplementedError


# Exercise 12
def merge_settings(
    defaults: dict[str, object],
    overrides: dict[str, object],
) -> dict[str, object]:
    """
    Merge dictionaries.

    Overrides must win.
    """
    # TODO: dictionary unpacking
    raise NotImplementedError


# ============================================================
# SECTION 5 — SORTING / KEY FUNCTIONS
# ============================================================


@dataclass
class Person:
    name: str
    age: int


# Exercise 13
def sort_people_by_age(people: list[Person]) -> list[Person]:
    """Return a new list sorted by age."""
    # TODO: sorted(..., key=...)
    raise NotImplementedError


# Exercise 14
def oldest_three(people: list[Person]) -> list[Person]:
    """Return the three oldest people, oldest first."""
    # TODO
    raise NotImplementedError


# ============================================================
# SECTION 6 — FUNCTIONS / ARGS / KWARGS
# ============================================================


# Exercise 15
def total(*numbers: float) -> float:
    """Return the total of arbitrary positional arguments."""
    # TODO
    raise NotImplementedError


# Exercise 16
def build_config(**options: object) -> dict[str, object]:
    """Return keyword arguments as a dictionary."""
    # TODO
    raise NotImplementedError


# Exercise 17
def call_twice(
    function: Callable[[int], int],
    value: int,
) -> int:
    """
    Call function twice:

        function(function(value))
    """
    # TODO
    raise NotImplementedError


# ============================================================
# SECTION 7 — CLOSURES
# ============================================================


# Exercise 18
def multiplier(factor: int) -> Callable[[int], int]:
    """
    multiplier(3)(10) == 30

    Implement using a closure.
    """
    # TODO
    raise NotImplementedError


# Exercise 19 — Python trap
def make_multipliers() -> list[Callable[[int], int]]:
    """
    Return three functions:

        functions[0](10) == 10
        functions[1](10) == 20
        functions[2](10) == 30

    Beware late-binding closures.
    """
    # TODO
    raise NotImplementedError


# ============================================================
# SECTION 8 — ITERATORS / GENERATORS
# ============================================================


# Exercise 20
def countdown(start: int) -> Generator[int, None, None]:
    """Yield start ... 1."""
    # TODO: yield
    raise NotImplementedError


# Exercise 21
def batches(
    items: list[int],
    size: int,
) -> Iterator[list[int]]:
    """
    batches([1,2,3,4,5], 2)

    yields:
        [1,2]
        [3,4]
        [5]
    """
    # TODO
    raise NotImplementedError


# Exercise 22
def flatten(groups: Iterable[Iterable[int]]) -> Iterator[int]:
    """Lazily flatten nested iterables."""
    # TODO
    raise NotImplementedError


# ============================================================
# SECTION 9 — DATACLASSES
# ============================================================


# Exercise 23
@dataclass
class User:
    id: int
    name: str
    active: bool = True

    # TODO:
    # Add a method deactivate() -> None
    pass


# Exercise 24
@dataclass(frozen=True)
class Coordinate:
    x: float
    y: float


# Question:
# What does frozen=True change?
# Be able to explain it aloud.


# ============================================================
# SECTION 10 — CLASSES
# ============================================================


# Exercise 25
class BankAccount:

    bank_name: ClassVar[str] = "Python Bank"

    def __init__(self, owner: str, balance: float = 0) -> None:
        # TODO
        pass

    @property
    def balance(self) -> float:
        # TODO
        raise NotImplementedError

    def deposit(self, amount: float) -> None:
        # TODO
        pass

    def withdraw(self, amount: float) -> None:
        """
        Raise ValueError if insufficient funds.
        """
        # TODO
        pass

    @classmethod
    def empty(cls, owner: str) -> Self:
        # TODO
        raise NotImplementedError

    @staticmethod
    def valid_amount(amount: float) -> bool:
        # TODO
        raise NotImplementedError


# ============================================================
# SECTION 11 — ABSTRACT BASE CLASSES
# ============================================================


# Exercise 26
class Serializer(ABC):

    @abstractmethod
    def serialize(self, value: object) -> str:
        ...


class StringSerializer(Serializer):

    def serialize(self, value: object) -> str:
        # TODO
        raise NotImplementedError


# ============================================================
# SECTION 12 — BASIC TYPING
# ============================================================


# Exercise 27
def find_user(
    users: Iterable[User],
    user_id: int,
) -> User | None:
    """Return matching user or None."""
    # TODO
    raise NotImplementedError


# Exercise 28
T = TypeVar("T")


def first(items: Iterable[T]) -> T | None:
    """Generic first() function."""
    # TODO
    raise NotImplementedError


# ============================================================
# SECTION 13 — GENERICS
# ============================================================


TEntity = TypeVar("TEntity")


# Exercise 29
class MemoryRepository(Generic[TEntity]):

    def __init__(self) -> None:
        # TODO
        pass

    def add(self, entity: TEntity) -> None:
        # TODO
        pass

    def all(self) -> list[TEntity]:
        # TODO
        raise NotImplementedError


# ============================================================
# SECTION 14 — PROTOCOLS
# ============================================================


# Exercise 30

T_co = TypeVar("T_co", covariant=True)


class Reader(Protocol[T_co]):

    def read(self) -> T_co:
        ...


class NumberReader:

    def read(self) -> int:
        return 42


def perform_read(reader: Reader[int]) -> int:
    # TODO
    raise NotImplementedError


# Question:
#
# Why does NumberReader satisfy Reader[int] even though it
# doesn't inherit from Reader?
#
# Know the phrase:
#
#     structural typing


# ============================================================
# SECTION 15 — TYPEDDICT / LITERAL
# ============================================================


class UserPayload(TypedDict):
    name: str
    age: int


Status = Literal["pending", "running", "complete"]


# Exercise 31
def create_user(payload: UserPayload) -> User:
    # TODO
    raise NotImplementedError


# Exercise 32
def describe_status(status: Status) -> str:
    # TODO
    raise NotImplementedError


# ============================================================
# SECTION 16 — CAST / TYPE NARROWING
# ============================================================


# Exercise 33
def string_length(value: object) -> int:
    """
    Return string length.

    Raise TypeError if value isn't a string.

    Let isinstance() narrow the type.
    """
    # TODO
    raise NotImplementedError


# Exercise 34
def force_string(value: object) -> str:
    """
    Use cast().

    IMPORTANT:
    Be able to explain why cast() does NOT perform runtime conversion.
    """
    # TODO
    raise NotImplementedError


# ============================================================
# SECTION 17 — OVERLOAD
# ============================================================


@overload
def convert(value: int) -> str:
    ...


@overload
def convert(value: str) -> int:
    ...


# Exercise 35
def convert(value: int | str) -> str | int:
    """
    int -> str
    str -> int
    """
    # TODO
    raise NotImplementedError


# ============================================================
# SECTION 18 — EXCEPTIONS
# ============================================================


class InvalidAgeError(ValueError):
    pass


# Exercise 36
def validate_age(age: int) -> int:
    """
    Valid range: 0..130

    Raise InvalidAgeError otherwise.
    """
    # TODO
    raise NotImplementedError


# ============================================================
# SECTION 19 — CONTEXT MANAGERS
# ============================================================


# Exercise 37
@contextmanager
def timer() -> Iterator[Callable[[], float]]:
    """
    Usage:

        with timer() as elapsed:
            ...

        print(elapsed())

    elapsed() should return seconds since entering the context.
    """
    # TODO
    raise NotImplementedError


# ============================================================
# SECTION 20 — DECORATORS
# ============================================================


# Exercise 38
def repeat(times: int):
    """
    Decorator causing a function to execute N times.

    Preserve the original function metadata with functools.wraps.
    """

    # TODO
    raise NotImplementedError


# ============================================================
# SECTION 21 — ASYNC BASICS
# ============================================================


# Exercise 39
async def async_double(value: int) -> int:
    await asyncio.sleep(0.01)

    # TODO
    raise NotImplementedError


# Exercise 40
async def double_all(numbers: Iterable[int]) -> list[int]:
    """
    Run async_double() concurrently.

    Use asyncio.gather().
    """
    # TODO
    raise NotImplementedError


# ============================================================
# SECTION 22 — CREATE_TASK
# ============================================================


# Exercise 41
async def task_example(value: int) -> int:
    """
    Explicitly create a Task around async_double() and await it.
    """
    # TODO
    raise NotImplementedError


# ============================================================
# SECTION 23 — AS_COMPLETED
# ============================================================


async def delayed_value(value: int, delay: float) -> int:
    await asyncio.sleep(delay)
    return value


# Exercise 42
async def completion_order() -> list[int]:
    """
    Run concurrently:

        delayed_value(1, .03)
        delayed_value(2, .01)
        delayed_value(3, .02)

    Return results IN COMPLETION ORDER.

    Expected:
        [2, 3, 1]

    Hint:
        asyncio.as_completed
    """
    # TODO
    raise NotImplementedError


# ============================================================
# SECTION 24 — ASYNC EXCEPTIONS
# ============================================================


async def risky_operation(value: int) -> int:
    await asyncio.sleep(0)

    if value < 0:
        raise ValueError("negative value")

    return value * 2


# Exercise 43
async def safe_operation(value: int) -> int | None:
    """Return None if risky_operation raises ValueError."""
    # TODO
    raise NotImplementedError


# ============================================================
# SECTION 25 — CONCURRENCY LIMITS
# ============================================================


# Exercise 44
async def limited_double(
    numbers: Iterable[int],
    concurrency: int,
) -> list[int]:
    """
    Run async_double concurrently, but allow at most
    `concurrency` operations at once.

    Hint:
        asyncio.Semaphore
        async with
    """
    # TODO
    raise NotImplementedError


# ============================================================
# SECTION 26 — ASYNC ITERATORS
# ============================================================


# Exercise 45
class AsyncCounter:

    def __init__(self, limit: int) -> None:
        self.limit = limit
        self.current = 0

    def __aiter__(self) -> AsyncIterator[int]:
        # TODO
        raise NotImplementedError

    async def __anext__(self) -> int:
        # TODO
        raise NotImplementedError


async def consume_counter(limit: int) -> list[int]:
    result: list[int] = []

    async for value in AsyncCounter(limit):
        result.append(value)

    return result


# ============================================================
# SECTION 27 — ASYNC CONTEXT MANAGERS
# ============================================================


# Exercise 46
@asynccontextmanager
async def connection():
    """
    Simulate acquiring and releasing a connection.

    Yield the string:
        "CONNECTED"
    """

    # TODO
    raise NotImplementedError


async def use_connection() -> str:
    async with connection() as conn:
        return conn


# ============================================================
# SECTION 28 — ASYNC GENERATORS
# ============================================================


# Exercise 47
async def async_numbers(limit: int) -> AsyncIterator[int]:
    """
    Yield 0..limit-1 asynchronously.
    """
    # TODO
    raise NotImplementedError


# ============================================================
# SECTION 29 — CANCELLATION
# ============================================================


async def long_operation() -> None:
    await asyncio.sleep(10)


# Exercise 48
async def cancellation_example() -> bool:
    """
    Create long_operation as a task.

    Cancel it immediately.

    Await it and catch asyncio.CancelledError.

    Return True when cancellation was successfully observed.
    """
    # TODO
    raise NotImplementedError


# ============================================================
# SECTION 30 — TYPED ASYNC REPOSITORY
# ============================================================


EntityT = TypeVar("EntityT")


class AsyncRepository(Protocol[EntityT]):

    async def get(self, entity_id: int) -> EntityT | None:
        ...

    async def save(self, entity: EntityT) -> None:
        ...


# Exercise 49
class UserRepository:

    def __init__(self) -> None:
        self.users: dict[int, User] = {}

    async def get(self, entity_id: int) -> User | None:
        # TODO
        raise NotImplementedError

    async def save(self, entity: User) -> None:
        # TODO
        pass


# Exercise 50
async def deactivate_user(
    repository: AsyncRepository[User],
    user_id: int,
) -> bool:
    """
    1. Get user.
    2. Return False if nonexistent.
    3. Deactivate user.
    4. Save user.
    5. Return True.

    This combines:
        typing
        Protocol
        async
        classes
        control flow
    """

    # TODO
    raise NotImplementedError


# ============================================================
# SECTION 31 — REALISTIC MINI EXERCISE
# ============================================================


@dataclass
class Product:
    id: int
    name: str
    price: float
    active: bool = True


@dataclass
class OrderItem:
    product_id: int
    quantity: int


@dataclass
class OrderSummary:
    total: float
    missing_products: list[int]


class ProductRepository(Protocol):

    async def get(self, product_id: int) -> Product | None:
        ...


# Exercise 51
async def calculate_order(
    repository: ProductRepository,
    items: Iterable[OrderItem],
) -> OrderSummary:
    """
    FINAL EXERCISE

    Fetch products concurrently.

    Rules:

    - Fetch every product concurrently.
    - Ignore inactive products.
    - Missing products go into missing_products.
    - total = price * quantity.
    - Return OrderSummary.
    - Preserve the order of missing product IDs.

    Think about:

        list comprehensions
        zip
        typing
        protocols
        asyncio.gather
        dataclasses
        readability
        separating concerns

    Don't try to be clever.

    Write boring, readable production code.
    """

    # TODO
    raise NotImplementedError


# ============================================================
# TESTS
# ============================================================


def run_sync_tests() -> None:

    assert even_numbers([1, 2, 3, 4]) == [2, 4]

    assert unique_words(["Hello", "HELLO", "World"]) == {
        "hello",
        "world",
    }

    assert word_lengths(["cat", "python"]) == {
        "cat": 3,
        "python": 6,
    }

    assert swap(("hello", 42)) == (42, "hello")

    assert squares([1, 2, 3]) == [1, 4, 9]

    users = [
        {"name": "Alice", "active": True},
        {"name": "Bob", "active": False},
        {"name": "CHARLIE", "active": True},
    ]

    assert active_usernames(users) == ["alice", "charlie"]

    assert invert({"a": 1, "b": 2}) == {
        1: "a",
        2: "b",
    }

    assert numbered(["a", "b"]) == [
        (1, "a"),
        (2, "b"),
    ]

    assert combine(["a", "b"], [10, 20]) == [
        ("a", 10),
        ("b", 20),
    ]

    assert score_dictionary(
        ["Alice", "Bob"],
        [10, 20],
    ) == {
        "Alice": 10,
        "Bob": 20,
    }

    assert first_middle_last([1, 2, 3, 4]) == (
        1,
        [2, 3],
        4,
    )

    assert merge_settings(
        {"debug": False, "port": 80},
        {"debug": True},
    ) == {
        "debug": True,
        "port": 80,
    }

    people = [
        Person("Alice", 40),
        Person("Bob", 20),
        Person("Charlie", 30),
        Person("Dave", 50),
    ]

    assert [p.name for p in sort_people_by_age(people)] == [
        "Bob",
        "Charlie",
        "Alice",
        "Dave",
    ]

    assert [p.name for p in oldest_three(people)] == [
        "Dave",
        "Alice",
        "Charlie",
    ]

    assert total(1, 2, 3.5) == 6.5

    assert build_config(debug=True, port=8000) == {
        "debug": True,
        "port": 8000,
    }

    assert call_twice(lambda x: x * 2, 3) == 12

    times_three = multiplier(3)
    assert times_three(10) == 30

    funcs = make_multipliers()
    assert [f(10) for f in funcs] == [10, 20, 30]

    assert list(countdown(3)) == [3, 2, 1]

    assert list(batches([1, 2, 3, 4, 5], 2)) == [
        [1, 2],
        [3, 4],
        [5],
    ]

    assert list(flatten([[1, 2], [3], [4, 5]])) == [
        1,
        2,
        3,
        4,
        5,
    ]

    user = User(1, "Alice")
    user.deactivate()
    assert user.active is False

    account = BankAccount("Rodrigo", 100)

    account.deposit(50)
    assert account.balance == 150

    account.withdraw(25)
    assert account.balance == 125

    empty = BankAccount.empty("Alice")
    assert empty.balance == 0

    assert BankAccount.valid_amount(10)
    assert not BankAccount.valid_amount(-1)

    serializer = StringSerializer()
    assert serializer.serialize(123) == "123"

    users2 = [
        User(1, "Alice"),
        User(2, "Bob"),
    ]

    assert find_user(users2, 2) == users2[1]
    assert find_user(users2, 999) is None

    assert first([10, 20, 30]) == 10
    assert first([]) is None

    repo: MemoryRepository[str] = MemoryRepository()
    repo.add("hello")
    repo.add("world")

    assert repo.all() == ["hello", "world"]

    reader = NumberReader()
    assert perform_read(reader) == 42

    created = create_user({
        "name": "Alice",
        "age": 30,
    })

    assert created.name == "Alice"

    assert describe_status("pending") == "Status: pending"

    assert string_length("hello") == 5

    try:
        string_length(123)
        assert False
    except TypeError:
        pass

    assert force_string("hello") == "hello"

    assert convert(123) == "123"
    assert convert("123") == 123

    assert validate_age(30) == 30

    try:
        validate_age(200)
        assert False
    except InvalidAgeError:
        pass

    with timer() as elapsed:
        time.sleep(0.01)

    assert elapsed() >= 0.01

    calls: list[str] = []

    @repeat(3)
    def hello() -> None:
        calls.append("hello")

    hello()

    assert calls == [
        "hello",
        "hello",
        "hello",
    ]


class FakeProductRepository:

    def __init__(self) -> None:
        self.products = {
            1: Product(1, "Keyboard", 100),
            2: Product(2, "Mouse", 50),
            3: Product(3, "Old Monitor", 200, active=False),
        }

    async def get(self, product_id: int) -> Product | None:
        await asyncio.sleep(0.001)
        return self.products.get(product_id)


async def run_async_tests() -> None:

    assert await async_double(10) == 20

    assert await double_all([1, 2, 3]) == [
        2,
        4,
        6,
    ]

    assert await task_example(5) == 10

    assert await completion_order() == [2, 3, 1]

    assert await safe_operation(5) == 10
    assert await safe_operation(-1) is None

    assert await limited_double(
        [1, 2, 3, 4],
        concurrency=2,
    ) == [
        2,
        4,
        6,
        8,
    ]

    assert await consume_counter(3) == [
        0,
        1,
        2,
    ]

    assert await use_connection() == "CONNECTED"

    values = [
        value
        async for value in async_numbers(3)
    ]

    assert values == [0, 1, 2]

    assert await cancellation_example() is True

    repository = UserRepository()

    await repository.save(User(1, "Alice"))

    result = await deactivate_user(repository, 1)

    assert result is True

    stored = await repository.get(1)

    assert stored is not None
    assert stored.active is False

    assert await deactivate_user(repository, 999) is False

    product_repo = FakeProductRepository()

    summary = await calculate_order(
        product_repo,
        [
            OrderItem(1, 2),   # 200
            OrderItem(2, 3),   # 150
            OrderItem(3, 10),  # inactive
            OrderItem(999, 1), # missing
        ],
    )

    assert summary.total == 350
    assert summary.missing_products == [999]


# ============================================================
# RUNNER
# ============================================================


async def main() -> None:

    print("Running synchronous exercises...")
    run_sync_tests()

    print("Synchronous exercises passed.")

    print("Running asynchronous exercises...")
    await run_async_tests()

    print("Asynchronous exercises passed.")

    print()
    print("=" * 60)
    print("ALL EXERCISES PASSED")
    print("=" * 60)


if __name__ == "__main__":
    asyncio.run(main())
