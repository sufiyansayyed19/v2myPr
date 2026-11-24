from datetime import datetime
from uuid import UUID

from sqlalchemy import DateTime, ForeignKey, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class AuthIdentity(Base):
    __tablename__ = "auth_identities"

    id: Mapped[UUID] = mapped_column(primary_key=True)

    user_id: Mapped[UUID] = mapped_column(
        ForeignKey("users.id"),
        nullable=False,
        index=True
    )

    provider: Mapped[str] = mapped_column(
        String(30),
        nullable=False
    )

    provider_subject: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    provider_email: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False
    )

    __table_args__ = (
        UniqueConstraint(
            "provider",
            "provider_subject",
            name="uq_auth_identity_provider_subject"
        ),
    )