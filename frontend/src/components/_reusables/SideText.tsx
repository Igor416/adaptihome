interface SideTextProps {
  text: string,
  right: string
}

export default function SideText({text, right}: SideTextProps) {
  return <div
    style={{
      top: '80vh', 
      right: `-${right}vw`,
      transform: 'rotate(-90deg)'
    }}
    className='position-absolute overflow-hidden'
  >
    <span
      style={{
        opacity: 0.2,
        fontSize: '15vw',
        transform: 'translateY(5vw)'
      }}
      className='d-block text-blue overflow-hidden'
    >{text}</span>
  </div>
}