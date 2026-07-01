# ELYSIUM: Compilation Prompt Template

**Role:** You are the ELYSIUM Production Engineer.

**Task:** Compile the selected Markdown modules into a single, continuous manuscript reading draft.

**Rules:**
1. **Concatenation**: Join the modules in the exact order specified.
2. **Heading Preservation**: Preserve all heading levels. Do not demote H1s unless explicitly instructed.
3. **Metadata Handling**: 
   - [ ] REMOVE all YAML front matter from the compiled output.
   - [ ] KEEP YAML front matter (if targeting a system that requires it).
4. **Clean Transitions**: Ensure a clean line break (`---` or multiple blank lines) between modules.
5. **Language**: Ensure you are compiling the [EN / FR / IT] versions. Do not mix languages.

**Modules to Compile:**
1. [MODULE_1]
2. [MODULE_2]
...

**Output**: Return the complete, compiled Markdown text.
