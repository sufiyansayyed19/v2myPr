from datetime import datetime
from uuid import UUID

from sqlalchemy import DateTime, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class VerificationCode(Base):
    __tablename__ = "verification_codes"

    id: Mapped[UUID] = mapped_column(primary_key=True)

    email: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        index=True
    )

    code_hash: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    expires_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False
    )

    attempt_count: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        default=0
    )

    consumed_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True
    )

    invalidated_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False
    )