const ProjectTeamPage = ({name,employeeId,role,location}={...props}) => {
  return (
    <>
    <div className="card">
        <p>{name} </p>
        <p>{employeeId}</p>
        <p>{role}</p>
        <p>{location}</p>

    </div>
    </>
  )
}

export default ProjectTeamPage