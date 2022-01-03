function getDateOnly(date) {
    return new Date(date.getFullYear(), date.getMonth(), date.getDate())
}

export { getDateOnly }