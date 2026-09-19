"""
Tests for python_gym.py

Install:
    python -m pip install pytest pytest-asyncio

Run everything:
    pytest -v

Run one exercise:
    pytest -v test_python_gym.py::test_01_even_numbers

Run one section:
    pytest -v -k "async"
"""

import asyncio
import time

import pytest

from exercises import (
    # Collections / comprehensions
    even_numbers,
    unique_words,
    word_lengths,
    swap,
    squares,
    active_usernames,
    invert,

    # enumerate / zip / unpacking
    numbered,
    combine,
    score_dictionary,
    first_middle_last,
    merge_settings,

    # sorting
    Person,
    sort_people_by_age,
    oldest_three,

    # functions
    total,
    build_config,
    call_twice,

    # closures
    multiplier,
    make_multipliers,

    # generators
    countdown,
    batches,
    flatten,

    # classes
    User,
    Coordinate,
    BankAccount,
    StringSerializer,

    # typing / generics
    find_user,
    first,
    MemoryRepository,
    NumberReader,
    perform_read,
    create_user,
    describe_status,
    string_length,
    force_string,
    convert,

    # exceptions / context managers / decorators
    InvalidAgeError,
    validate_age,
    timer,
    repeat,

    # async
    async_double,
    double_all,
    task_example,
    completion_order,
    safe_operation,
    limited_double,
    AsyncCounter,
    consume_counter,
    use_connection,
    async_numbers,
    cancellation_example,

    # async repository
    UserRepository,
    deactivate_user,

    # final exercise
    Product,
    OrderItem,
    OrderSummary,
    calculate_order,
)


# ============================================================
# 01 — COLLECTIONS
# ============================================================


def test_01_even_numbers():
    assert even_numbers([1, 2, 3, 4, 5, 6]) == [2, 4, 6]
    assert even_numbers([]) == []
    assert even_numbers([1, 3, 5]) == []
    assert even_numbers([-2, -1, 0, 1, 2]) == [-2, 0, 2]


def test_02_unique_words():
    assert unique_words(
        ["Hello", "HELLO", "World", "world"]
    ) == {"hello", "world"}

    assert unique_words([]) == set()


def test_03_word_lengths():
    assert word_lengths(["cat", "python", "a"]) == {
        "cat": 3,
        "python": 6,
        "a": 1,
    }

    assert word_lengths([]) == {}


def test_04_swap():
    assert swap(("hello", 42)) == (42, "hello")
    assert swap(("", 0)) == (0, "")


# ============================================================
# 02 — COMPREHENSIONS
# ============================================================


def test_05_squares():
    assert squares([1, 2, 3]) == [1, 4, 9]
    assert squares([-2, 0, 3]) == [4, 0, 9]
    assert squares([]) == []


def test_06_active_usernames():
    users = [
        {"name": "Alice", "active": True},
        {"name": "Bob", "active": False},
        {"name": "CHARLIE", "active": True},
    ]

    assert active_usernames(users) == [
        "alice",
        "charlie",
    ]


def test_07_invert():
    assert invert({
        "a": 1,
        "b": 2,
        "c": 3,
    }) == {
        1: "a",
        2: "b",
        3: "c",
    }

    assert invert({}) == {}


# ============================================================
# 03 — ENUMERATE / ZIP
# ============================================================


def test_08_numbered():
    assert numbered(["a", "b", "c"]) == [
        (1, "a"),
        (2, "b"),
        (3, "c"),
    ]

    assert numbered([]) == []


def test_09_combine():
    assert combine(
        ["Alice", "Bob"],
        [10, 20],
    ) == [
        ("Alice", 10),
        ("Bob", 20),
    ]


def test_10_score_dictionary():
    assert score_dictionary(
        ["Alice", "Bob"],
        [10, 20],
    ) == {
        "Alice": 10,
        "Bob": 20,
    }


# ============================================================
# 04 — UNPACKING
# ============================================================


def test_11_first_middle_last():
    assert first_middle_last(
        [1, 2, 3, 4, 5]
    ) == (
        1,
        [2, 3, 4],
        5,
    )

    assert first_middle_last([1, 2]) == (
        1,
        [],
        2,
    )


def test_12_merge_settings():
    defaults = {
        "debug": False,
        "port": 80,
        "host": "localhost",
    }

    overrides = {
        "debug": True,
        "port": 8000,
    }

    assert merge_settings(
        defaults,
        overrides,
    ) == {
        "debug": True,
        "port": 8000,
        "host": "localhost",
    }


# ============================================================
# 05 — SORTING
# ============================================================


@pytest.fixture
def people():
    return [
        Person("Alice", 40),
        Person("Bob", 20),
        Person("Charlie", 30),
        Person("Dave", 50),
    ]


def test_13_sort_people_by_age(people):
    result = sort_people_by_age(people)

    assert [person.name for person in result] == [
        "Bob",
        "Charlie",
        "Alice",
        "Dave",
    ]


def test_13_sort_does_not_modify_original(people):
    sort_people_by_age(people)

    assert [person.name for person in people] == [
        "Alice",
        "Bob",
        "Charlie",
        "Dave",
    ]


def test_14_oldest_three(people):
    result = oldest_three(people)

    assert [person.name for person in result] == [
        "Dave",
        "Alice",
        "Charlie",
    ]


# ============================================================
# 06 — FUNCTIONS
# ============================================================


def test_15_total():
    assert total(1, 2, 3) == 6
    assert total(1.5, 2.5) == 4
    assert total() == 0


def test_16_build_config():
    assert build_config(
        debug=True,
        port=8000,
    ) == {
        "debug": True,
        "port": 8000,
    }


def test_17_call_twice():
    assert call_twice(
        lambda value: value * 2,
        3,
    ) == 12


# ============================================================
# 07 — CLOSURES
# ============================================================


def test_18_multiplier():
    times_three = multiplier(3)
    times_ten = multiplier(10)

    assert times_three(5) == 15
    assert times_ten(5) == 50


def test_19_make_multipliers():
    functions = make_multipliers()

    assert len(functions) == 3

    assert [
        function(10)
        for function in functions
    ] == [
        10,
        20,
        30,
    ]


# ============================================================
# 08 — GENERATORS
# ============================================================


def test_20_countdown():
    assert list(countdown(5)) == [
        5,
        4,
        3,
        2,
        1,
    ]

    assert list(countdown(0)) == []


def test_21_batches():
    assert list(
        batches([1, 2, 3, 4, 5], 2)
    ) == [
        [1, 2],
        [3, 4],
        [5],
    ]

    assert list(
        batches([1, 2, 3], 10)
    ) == [
        [1, 2, 3],
    ]


def test_22_flatten():
    assert list(
        flatten([
            [1, 2],
            [],
            [3],
            [4, 5],
        ])
    ) == [
        1,
        2,
        3,
        4,
        5,
    ]


# ============================================================
# 09 — DATACLASSES
# ============================================================


def test_23_user_deactivate():
    user = User(
        id=1,
        name="Alice",
    )

    assert user.active is True

    user.deactivate()

    assert user.active is False


def test_24_coordinate_is_frozen():
    coordinate = Coordinate(
        x=10,
        y=20,
    )

    with pytest.raises(Exception):
        coordinate.x = 50


# ============================================================
# 10 — CLASSES
# ============================================================


def test_25_bank_account_creation():
    account = BankAccount(
        "Rodrigo",
        100,
    )

    assert account.balance == 100


def test_25_bank_account_deposit():
    account = BankAccount(
        "Rodrigo",
        100,
    )

    account.deposit(50)

    assert account.balance == 150


def test_25_bank_account_withdraw():
    account = BankAccount(
        "Rodrigo",
        100,
    )

    account.withdraw(30)

    assert account.balance == 70


def test_25_bank_account_insufficient_funds():
    account = BankAccount(
        "Rodrigo",
        100,
    )

    with pytest.raises(ValueError):
        account.withdraw(101)


def test_25_bank_account_empty_factory():
    account = BankAccount.empty("Alice")

    assert isinstance(account, BankAccount)
    assert account.balance == 0


@pytest.mark.parametrize(
    "amount,expected",
    [
        (10, True),
        (0.01, True),
        (0, False),
        (-1, False),
    ],
)
def test_25_valid_amount(amount, expected):
    assert BankAccount.valid_amount(amount) is expected


# ============================================================
# 11 — ABC
# ============================================================


def test_26_serializer():
    serializer = StringSerializer()

    assert serializer.serialize(123) == "123"
    assert serializer.serialize("hello") == "hello"
    assert serializer.serialize(True) == "True"


# ============================================================
# 12 — BASIC TYPING
# ============================================================


def test_27_find_user():
    users = [
        User(1, "Alice"),
        User(2, "Bob"),
    ]

    assert find_user(users, 2) == users[1]
    assert find_user(users, 999) is None


def test_28_generic_first():
    assert first([10, 20, 30]) == 10
    assert first(["a", "b"]) == "a"
    assert first([]) is None

    # Should work with arbitrary iterables,
    # not only lists.
    assert first(iter([100, 200])) == 100


# ============================================================
# 13 — GENERICS
# ============================================================


def test_29_memory_repository():
    repository: MemoryRepository[str] = (
        MemoryRepository()
    )

    repository.add("hello")
    repository.add("world")

    assert repository.all() == [
        "hello",
        "world",
    ]


def test_29_repository_does_not_expose_internal_list():
    repository: MemoryRepository[int] = (
        MemoryRepository()
    )

    repository.add(1)

    result = repository.all()
    result.append(999)

    # Prefer all() returning a copy rather than allowing
    # callers to mutate repository state.
    assert repository.all() == [1]


# ============================================================
# 14 — PROTOCOLS
# ============================================================


def test_30_protocol_reader():
    reader = NumberReader()

    assert perform_read(reader) == 42


def test_30_structural_typing():
    class DifferentReader:

        def read(self) -> int:
            return 123

    reader = DifferentReader()

    assert perform_read(reader) == 123


# ============================================================
# 15 — TYPEDDICT / LITERAL
# ============================================================


def test_31_create_user():
    user = create_user({
        "name": "Alice",
        "age": 30,
    })

    assert isinstance(user, User)
    assert user.name == "Alice"


def test_32_describe_status():
    assert describe_status(
        "pending"
    ) == "Status: pending"

    assert describe_status(
        "running"
    ) == "Status: running"

    assert describe_status(
        "complete"
    ) == "Status: complete"


# ============================================================
# 16 — TYPE NARROWING / CAST
# ============================================================


def test_33_string_length():
    assert string_length("hello") == 5
    assert string_length("") == 0


def test_33_string_length_rejects_non_string():
    with pytest.raises(TypeError):
        string_length(123)


def test_34_force_string():
    value = "hello"

    assert force_string(value) == "hello"


# ============================================================
# 17 — OVERLOAD
# ============================================================


def test_35_convert_integer():
    assert convert(123) == "123"


def test_35_convert_string():
    assert convert("123") == 123


# ============================================================
# 18 — EXCEPTIONS
# ============================================================


@pytest.mark.parametrize(
    "age",
    [
        0,
        1,
        50,
        130,
    ],
)
def test_36_validate_age(age):
    assert validate_age(age) == age


@pytest.mark.parametrize(
    "age",
    [
        -1,
        131,
        1000,
    ],
)
def test_36_validate_invalid_age(age):
    with pytest.raises(InvalidAgeError):
        validate_age(age)


# ============================================================
# 19 — CONTEXT MANAGERS
# ============================================================


def test_37_timer():
    with timer() as elapsed:
        time.sleep(0.02)

    assert elapsed() >= 0.02


def test_37_timer_returns_callable():
    with timer() as elapsed:
        assert callable(elapsed)


# ============================================================
# 20 — DECORATORS
# ============================================================


def test_38_repeat():
    calls = []

    @repeat(3)
    def hello():
        calls.append("hello")

    hello()

    assert calls == [
        "hello",
        "hello",
        "hello",
    ]


def test_38_repeat_preserves_metadata():
    @repeat(2)
    def my_function():
        """My documentation."""
        pass

    assert my_function.__name__ == "my_function"
    assert my_function.__doc__ == "My documentation."


# ============================================================
# 21 — ASYNC BASICS
# ============================================================


@pytest.mark.asyncio
async def test_39_async_double():
    assert await async_double(10) == 20
    assert await async_double(-5) == -10


@pytest.mark.asyncio
async def test_40_double_all():
    assert await double_all(
        [1, 2, 3]
    ) == [
        2,
        4,
        6,
    ]


@pytest.mark.asyncio
async def test_40_double_all_empty():
    assert await double_all([]) == []


# ============================================================
# 22 — CREATE_TASK
# ============================================================


@pytest.mark.asyncio
async def test_41_task_example():
    assert await task_example(10) == 20


# ============================================================
# 23 — AS_COMPLETED
# ============================================================


@pytest.mark.asyncio
async def test_42_completion_order():
    assert await completion_order() == [
        2,
        3,
        1,
    ]


# ============================================================
# 24 — ASYNC EXCEPTIONS
# ============================================================


@pytest.mark.asyncio
async def test_43_safe_operation_success():
    assert await safe_operation(10) == 20


@pytest.mark.asyncio
async def test_43_safe_operation_failure():
    assert await safe_operation(-1) is None


# ============================================================
# 25 — SEMAPHORE
# ============================================================


@pytest.mark.asyncio
async def test_44_limited_double():
    assert await limited_double(
        [1, 2, 3, 4],
        concurrency=2,
    ) == [
        2,
        4,
        6,
        8,
    ]


# ============================================================
# 26 — ASYNC ITERATORS
# ============================================================


@pytest.mark.asyncio
async def test_45_async_counter():
    result = []

    async for value in AsyncCounter(4):
        result.append(value)

    assert result == [
        0,
        1,
        2,
        3,
    ]


@pytest.mark.asyncio
async def test_45_consume_counter():
    assert await consume_counter(3) == [
        0,
        1,
        2,
    ]


# ============================================================
# 27 — ASYNC CONTEXT MANAGERS
# ============================================================


@pytest.mark.asyncio
async def test_46_connection():
    assert await use_connection() == "CONNECTED"


# ============================================================
# 28 — ASYNC GENERATORS
# ============================================================


@pytest.mark.asyncio
async def test_47_async_numbers():
    values = []

    async for value in async_numbers(4):
        values.append(value)

    assert values == [
        0,
        1,
        2,
        3,
    ]


# ============================================================
# 29 — CANCELLATION
# ============================================================


@pytest.mark.asyncio
async def test_48_cancellation():
    assert await cancellation_example() is True


# ============================================================
# 30 — ASYNC REPOSITORY
# ============================================================


@pytest.mark.asyncio
async def test_49_user_repository_save_and_get():
    repository = UserRepository()

    user = User(
        id=1,
        name="Alice",
    )

    await repository.save(user)

    result = await repository.get(1)

    assert result == user


@pytest.mark.asyncio
async def test_49_missing_user():
    repository = UserRepository()

    assert await repository.get(999) is None


@pytest.mark.asyncio
async def test_50_deactivate_user():
    repository = UserRepository()

    await repository.save(
        User(
            id=1,
            name="Alice",
        )
    )

    result = await deactivate_user(
        repository,
        1,
    )

    assert result is True

    user = await repository.get(1)

    assert user is not None
    assert user.active is False


@pytest.mark.asyncio
async def test_50_deactivate_missing_user():
    repository = UserRepository()

    result = await deactivate_user(
        repository,
        999,
    )

    assert result is False


# ============================================================
# 31 — FINAL EXERCISE
# ============================================================


class FakeProductRepository:

    def __init__(self):
        self.products = {
            1: Product(
                1,
                "Keyboard",
                100,
            ),
            2: Product(
                2,
                "Mouse",
                50,
            ),
            3: Product(
                3,
                "Old monitor",
                200,
                active=False,
            ),
        }

    async def get(
        self,
        product_id: int,
    ) -> Product | None:

        await asyncio.sleep(0.001)

        return self.products.get(product_id)


@pytest.mark.asyncio
async def test_51_calculate_order():
    repository = FakeProductRepository()

    result = await calculate_order(
        repository,
        [
            OrderItem(
                product_id=1,
                quantity=2,
            ),
            OrderItem(
                product_id=2,
                quantity=3,
            ),
        ],
    )

    assert isinstance(
        result,
        OrderSummary,
    )

    assert result.total == 350

    assert result.missing_products == []


@pytest.mark.asyncio
async def test_51_missing_products():
    repository = FakeProductRepository()

    result = await calculate_order(
        repository,
        [
            OrderItem(999, 1),
            OrderItem(1, 1),
            OrderItem(888, 1),
        ],
    )

    assert result.total == 100

    # Order must be preserved.
    assert result.missing_products == [
        999,
        888,
    ]


@pytest.mark.asyncio
async def test_51_inactive_products_are_ignored():
    repository = FakeProductRepository()

    result = await calculate_order(
        repository,
        [
            OrderItem(1, 1),
            OrderItem(3, 100),
        ],
    )

    # Product 3 exists but is inactive.
    assert result.total == 100

    # Inactive != missing.
    assert result.missing_products == []


@pytest.mark.asyncio
async def test_51_empty_order():
    repository = FakeProductRepository()

    result = await calculate_order(
        repository,
        [],
    )

    assert result.total == 0
    assert result.missing_products == []


# ============================================================
# BONUS — FINAL INTERVIEW-STYLE TEST
# ============================================================


@pytest.mark.asyncio
async def test_51_fetches_products_concurrently():
    """
    This catches an implementation such as:

        for item in items:
            product = await repository.get(...)

    which is sequential rather than concurrent.

    Five 50ms requests sequentially take roughly 250ms.
    Concurrent execution should take roughly 50ms.
    """

    class SlowRepository:

        async def get(
            self,
            product_id: int,
        ) -> Product:
            await asyncio.sleep(0.05)

            return Product(
                product_id,
                f"Product {product_id}",
                10,
            )

    repository = SlowRepository()

    items = [
        OrderItem(i, 1)
        for i in range(5)
    ]

    start = time.perf_counter()

    result = await calculate_order(
        repository,
        items,
    )

    elapsed = time.perf_counter() - start

    assert result.total == 50

    # Generous threshold to avoid flaky tests while still
    # distinguishing concurrent from ~250ms sequential code.
    assert elapsed < 0.18
