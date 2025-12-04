---

## **docs/api/routes.md**
```markdown
# 🌍 API Routes (HTTP Endpoints)

SSWG–MVM exposes a REST API for full workflow lifecycle operations.

---

## **POST /api/workflows/generate**
Create a workflow from input.

**Example Request**
```json
{
  "purpose": "Teach basic Python",
  "audience": "Beginners",
  "style": "Friendly"
}
