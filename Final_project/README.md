# Functional Calculator - Final Project

This project serves as a robust, menu-driven calculator developed for the **AI Programming** course at Tafila Technical University. 

This repository is part of my broader [Learning Portfolio]:
https://github.com/Mohammad-QT/Python_2

where I document my academic journey through Computer Science. You can find all my laboratory assignments, homework solutions, and study notes for this semester in that repository, reflecting the evolution of my coding skills from basic scripts to functional programming implementations.

--------------------------------------------------------------------------------------------------

## Project Overview
This project serves as a robust, menu-driven calculator. Unlike standard calculators, this implementation leverages **Lambda expressions, Dictionaries, and Higher-Order functions** to ensure code modularity, readability, and efficiency.

--------------------------------------------------------------------------------------------------

## Required Concepts & Implementation
Every aspect of this project was designed to satisfy the semester's academic requirements:

* **Core Logic:** Uses a `dictionary` of `lambda` expressions for clean, scalable operation handling.
* **Functional Programming:** Utilizes `map()`, `filter()`, and `zip()` for efficient list manipulation.
* **User Interaction:** Features a persistent `while` loop menu and error handling (e.g., division by zero).
* **Data Management:** Employs `lists` for history tracking and `sets` for unique result filtering.
* **Indexing:** Implements `enumerate()` to provide a user-friendly, indexed history view.

--------------------------------------------------------------------------------------------------

## Project Structure
The project is organized to maintain a clear flow of logic and functionality:

* **`final_project.py`**
  * The main execution script containing all functional blocks, menu logic, and calculations.
* **`README.md`**
  * Documentation of the project workflow, requirements, and features.
* **`Screenshots/`**
  * Visual demonstrations of the calculator in action.

--------------------------------------------------------------------------------------------------

## Key Functionalities

1. **Standard Calculation:** Uses a dictionary-mapped `lambda` approach for math operations.
2. **Batch Addition:** Employs `zip()` to perform element-wise addition on two lists.
3. **List Transformation:** Uses `map()` to double input values dynamically.
4. **History & Analysis:** * Tracks past operations using a list.
    * Uses `enumerate()` to display results chronologically.
    * Filters positive results using `filter()` and `lambda`.

--------------------------------------------------------------------------------------------------

## Operational Highlights

### 1. The "Lambda" Advantage
By mapping operators (`+`, `-`, `*`, `/`, `^`) directly to `lambda` functions within a dictionary, we eliminated the need for long, repetitive `if-elif` chains, adhering to "Clean Code" principles.

### 2. Handling Complex Data
A major challenge was processing mixed list inputs. By combining `map(float, ...)` with `lambda`, we ensured that user input is correctly cast and processed regardless of the numerical format.

--------------------------------------------------------------------------------------------------

## Academic Compliance
* **Course:** AI Programming (Tafila Technical University)
* **Status:** Final Project
* **Student:** Mohammad Ismael Salman Al-Qatameen

> **Note:** This project is for educational purposes. It demonstrates the application of functional Python concepts in a real-world, small-scale utility context.

Study Philosophy: I believe that coding is a craft that requires constant practice. My study repository tracks my daily progress, from solving simple logical puzzles in early labs to building complex functional architectures in final projects like this one.