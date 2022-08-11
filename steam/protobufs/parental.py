# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: steammessages_parental.steamclient.proto
# plugin: python-betterproto
# Last updated 09/09/2021

from dataclasses import dataclass

import betterproto


@dataclass(eq=False, repr=False)
class ParentalApp(betterproto.Message):
    appid: int = betterproto.uint32_field(1)
    is_allowed: bool = betterproto.bool_field(2)


@dataclass(eq=False, repr=False)
class ParentalSettings(betterproto.Message):
    steamid: int = betterproto.fixed64_field(1)
    applist_base_id: int = betterproto.uint32_field(2)
    applist_base_description: str = betterproto.string_field(3)
    applist_base: "list[ParentalApp]" = betterproto.message_field(4)
    applist_custom: "list[ParentalApp]" = betterproto.message_field(5)
    passwordhashtype: int = betterproto.uint32_field(6)
    salt: bytes = betterproto.bytes_field(7)
    passwordhash: bytes = betterproto.bytes_field(8)
    is_enabled: bool = betterproto.bool_field(9)
    enabled_features: int = betterproto.uint32_field(10)
    recovery_email: str = betterproto.string_field(11)
    is_site_license_lock: bool = betterproto.bool_field(12)


@dataclass(eq=False, repr=False)
class EnableParentalSettingsRequest(betterproto.Message):
    password: str = betterproto.string_field(1)
    settings: "ParentalSettings" = betterproto.message_field(2)
    sessionid: str = betterproto.string_field(3)
    enablecode: int = betterproto.uint32_field(4)
    steamid: int = betterproto.fixed64_field(10)


@dataclass(eq=False, repr=False)
class EnableParentalSettingsResponse(betterproto.Message):
    pass


@dataclass(eq=False, repr=False)
class DisableParentalSettingsRequest(betterproto.Message):
    password: str = betterproto.string_field(1)
    steamid: int = betterproto.fixed64_field(10)


@dataclass(eq=False, repr=False)
class DisableParentalSettingsResponse(betterproto.Message):
    pass


@dataclass(eq=False, repr=False)
class GetParentalSettingsRequest(betterproto.Message):
    steamid: int = betterproto.fixed64_field(10)


@dataclass(eq=False, repr=False)
class GetParentalSettingsResponse(betterproto.Message):
    settings: "ParentalSettings" = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class GetSignedParentalSettingsRequest(betterproto.Message):
    priority: int = betterproto.uint32_field(1)


@dataclass(eq=False, repr=False)
class GetSignedParentalSettingsResponse(betterproto.Message):
    serialized_settings: bytes = betterproto.bytes_field(1)
    signature: bytes = betterproto.bytes_field(2)


@dataclass(eq=False, repr=False)
class SetParentalSettingsRequest(betterproto.Message):
    password: str = betterproto.string_field(1)
    settings: "ParentalSettings" = betterproto.message_field(2)
    new_password: str = betterproto.string_field(3)
    sessionid: str = betterproto.string_field(4)
    steamid: int = betterproto.fixed64_field(10)


@dataclass(eq=False, repr=False)
class SetParentalSettingsResponse(betterproto.Message):
    pass


@dataclass(eq=False, repr=False)
class ValidateTokenRequest(betterproto.Message):
    unlock_token: str = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class ValidateTokenResponse(betterproto.Message):
    pass


@dataclass(eq=False, repr=False)
class ValidatePasswordRequest(betterproto.Message):
    password: str = betterproto.string_field(1)
    session: str = betterproto.string_field(2)
    send_unlock_on_success: bool = betterproto.bool_field(3)


@dataclass(eq=False, repr=False)
class ValidatePasswordResponse(betterproto.Message):
    token: str = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class LockClientRequest(betterproto.Message):
    session: str = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class LockClientResponse(betterproto.Message):
    pass


@dataclass(eq=False, repr=False)
class RequestRecoveryCodeRequest(betterproto.Message):
    pass


@dataclass(eq=False, repr=False)
class RequestRecoveryCodeResponse(betterproto.Message):
    pass


@dataclass(eq=False, repr=False)
class DisableWithRecoveryCodeRequest(betterproto.Message):
    recovery_code: int = betterproto.uint32_field(1)
    steamid: int = betterproto.fixed64_field(10)


@dataclass(eq=False, repr=False)
class DisableWithRecoveryCodeResponse(betterproto.Message):
    pass


@dataclass(eq=False, repr=False)
class ParentalSettingsChangeNotification(betterproto.Message):
    serialized_settings: bytes = betterproto.bytes_field(1)
    signature: bytes = betterproto.bytes_field(2)
    password: str = betterproto.string_field(3)
    sessionid: str = betterproto.string_field(4)


@dataclass(eq=False, repr=False)
class ParentalUnlockNotification(betterproto.Message):
    password: str = betterproto.string_field(1)
    sessionid: str = betterproto.string_field(2)


@dataclass(eq=False, repr=False)
class ParentalLockNotification(betterproto.Message):
    sessionid: str = betterproto.string_field(1)
