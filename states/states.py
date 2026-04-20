from aiogram.fsm.state import State, StatesGroup


class Registration(StatesGroup):
    full_name = State()
    phone     = State()


class ExamBooking(StatesGroup):
    selecting_type = State()
    selecting_date = State()
    confirming     = State()


class AdminStates(StatesGroup):
    # ── Add exam type (bug fix: now includes description step)
    adding_type_name        = State()
    adding_type_description = State()

    # ── Edit exam type
    editing_type_name        = State()
    editing_type_description = State()

    # ── Add exam date
    adding_date_type     = State()
    adding_date_value    = State()
    adding_date_location = State()
    adding_date_seats    = State()

    # ── Edit exam date
    editing_date_value    = State()
    editing_date_location = State()
    editing_date_seats    = State()

    # ── Broadcast (extended)
    broadcast_select_type  = State()   # selecting exam type for targeted broadcast
    broadcast_select_date  = State()   # selecting exam date for targeted broadcast
    broadcast_text         = State()
    broadcast_confirm      = State()
