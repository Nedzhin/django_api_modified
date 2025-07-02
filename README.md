# Django API Extension - Instruction Endpoint

## Approach
- Added an APIView to list `Instruction`s for a given GP Surgery.
- Supports filtering by `instruction_type`, `start_date`, and `end_date`.
- Custom serializer includes nested fields: patient full name, GP name, and instruction type name.

## How to Use
`GET /api/instructions/<surgery_id>/?instruction_type=Referral&start_date=2024-01-01&end_date=2024-12-31`

## Assumptions
- `Instruction` has foreign keys to `Patient`, `GP`, and `InstructionType`.
- `GP` is linked to `GPSurgery`.

## AI Tools Used
This implementation was assisted by ChatGPT for architecture planning and syntax review.
# django_api_modified
