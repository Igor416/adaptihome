import { t } from "i18next"
import PlusIcon from "../Shop/PlusIcon"
import { DetailedProduct } from "../../JSONTypes"
import { ReactNode } from "react"

interface SectionProps {
  id: string,
  title: string,
  opened: boolean,
  open: () => void,
  children: ReactNode[]
}

export default function Section({id, title, opened, open, children}: SectionProps) {
  return <div className='accordion-item d-flex flex-column border-start-0 border-bottom-0 border-end-0 border-top mt-4 py-4'>
    <div
      onClick={open}
      className='accordion-header d-flex justify-content-between align-items-end'
      aria-expanded='false'
      data-bs-toggle='collapse'
      data-bs-target={'#' + id}
    >
      <span className='h5'>{title}</span>
      <PlusIcon size={1} active={opened} />
    </div>
    <div id={id} className='accordion-collapse collapse flex-column h6' data-bs-parent='#details'>
      {children}
    </div>
  </div>
}