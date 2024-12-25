"use client"
import React, { useState, useEffect } from "react";

export default function Home() {

  const [allAssignments, setAllAssignments] = useState([]);
  useEffect(() => {
    fetch('http://127.0.0.1:5000/getall').then((res) => res.json()).then((data) => {
      setAllAssignments(data.all_assignments)
    })
  }, [])

  const [toDelete, setToDelete] = useState("")
  const handleInputChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setToDelete(event.target.value)
  }

  const [nameToAdd, setNameToAdd] = useState("")
  const handleInputChange2 = (event: React.ChangeEvent<HTMLInputElement>) => {
    setNameToAdd(event.target.value)
  }

  const [courseToAdd, setCourseToAdd] = useState("")
  const handleInputChange3 = (event: React.ChangeEvent<HTMLInputElement>) => {
    setCourseToAdd(event.target.value)
  }

  const [nameToUpdate, setNameToUpdate] = useState("")
  const handleInputChange4 = (event: React.ChangeEvent<HTMLInputElement>) => {
    setNameToUpdate(event.target.value)
  }

  const [newGrade, setNewGrade] = useState("")
  const handleInputChange5 = (event: React.ChangeEvent<HTMLInputElement>) => {
    setNewGrade(event.target.value)
  }

  function deleteButton() {
    fetch(`http://127.0.0.1:5000/delete/${toDelete}`, {method: "DELETE"})
  }

  function addButton() {
    fetch(`http://127.0.0.1:5000/create/${nameToAdd}/${courseToAdd}`, {method: "POST"})
  }

  function updateButton() {
    fetch(`http://127.0.0.1:5000/update/${nameToUpdate}/${newGrade}`, {method: "PUT"})
  }

  return (
    <div className="grid grid-rows-[20px_1fr_20px] items-center justify-items-center min-h-screen p-8 pb-20 gap-16 sm:p-20 font-[family-name:var(--font-geist-sans)]">
      <main className="flex flex-col gap-8 row-start-2 items-center sm:items-start">
        <ul>
          <li>
          {allAssignments.map(allAssignments => 
          <div key={allAssignments.assignment_name}>
            {allAssignments.assignment_name} - {allAssignments.course_code} - {allAssignments.grade}%
            </div>)}
            </li>
        </ul>
        <div className="flex gap-4 items-center flex-col sm:flex-row">
          <input
            onChange={handleInputChange}
            placeholder="assignment to delete"
          /> 
          <button onClick={deleteButton}>delete</button>
        </div>
        <div>
          <input
            placeholder="name"
            onChange={handleInputChange2}
          />
          <input
            placeholder='course'
            onChange={handleInputChange3}
          />
          <button onClick={addButton}>add</button>
        </div>
        <div>
          <input
            placeholder="name"
            onChange={handleInputChange4}
          />
          <input
            placeholder='new grade'
            onChange={handleInputChange5}
          />
          <button onClick={updateButton}>update grade</button>
        </div>
      </main>
    </div>
  );
}
