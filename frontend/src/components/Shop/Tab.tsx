import PlusIcon from "./PlusIcon"

interface TabProps {
  setter: (val: boolean) => void,
  active: boolean,
  text: string,
  direction: '' | '-reverse'
}

export default function Tab({setter, active, text, direction}: TabProps) {
  return <div className={'py-4 p-sm-5 col-6 d-flex border-end flex-row' + direction}>
    <div className='col-sm-6'></div>
    <div
      onClick={() => setter(!active)}
      className='col-12 col-sm-6 d-flex justify-content-center justify-content-sm-between align-items-end'
    >
      <span className='me-sm-0 me-2'>{text}</span>
      <PlusIcon size={2} active={active} />
    </div>
  </div>
}