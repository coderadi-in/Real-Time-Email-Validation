# REAL-TIME EMAIL VALIDATION

## TECH STACK

<div style="display: flex; align-items: center; gap: 20px;">
    <img src="docs/ctk.png" width="30">
    <span>CustomTkinter</span>
</div>

---

<div style="display: flex; align-items: center; gap: 20px;">
    <img src="docs/python.png" width="30">
    <span>Python</span>
</div>

---

## WHAT MAKES IT WORK

```py
# * Function to validate email
def check_validation(event=None):
    email = event.widget.get()
    pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    valid = re.search(pattern, email)

    if (not valid) and (email != ""):
        warning.grid(row=6, column=0, sticky="w", padx=5, pady=(0, 5))

    else:warning.grid_forget()
```

The `re` module of Python checks out the pattern.
```python
pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
```

### Example

Let's checkout this email with the pattern: `someone123.some@example.com`.
- `someone123.some` is covered under `[a-zA-Z0-9._%+-]` part of pattern.
- `@` is covered under `+@` part.
- `example` is covered under `[a-zA-Z0-9.-]`.
- `.` under `+\.`.
- And `com` us covered under `[a-zA-Z]{2,}` part of the pattern.

### HOW IT WORKS IN REAL-TIME

```py
email.bind("<KeyRelease>", check_validation)
```

The `"<KeyRelease>"` event call the `check_validation` function everytime the user Releases the Key (after pressing).