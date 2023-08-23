interface CircleProps {
  size: number,
  color: string
  active: boolean,
  setActive: () => void
}

export default function Circle({size, color, active, setActive}: CircleProps) {
  return <div
    onClick={setActive}
    style={{width: size + 'vw', aspectRatio: 1}}
    className='position-relative rounded-circle d-flex justify-content-center align-items-center'
  >
    <div
      style={{
        zIndex: 1100,
        width: size / 5 + 'vw',
        aspectRatio: 1
      }}
      className={'position-relative rounded-circle transition bg-' + (active ? 'white' : 'blue')}></div>
    <div
      style={{
        transform: `scale(${active ? 1 : 0})`,
        transformOrigin: 'center'
      }}
      className={'position-absolute rounded-circle w-100 h-100 transition bg-' + color}></div>
  </div>
}