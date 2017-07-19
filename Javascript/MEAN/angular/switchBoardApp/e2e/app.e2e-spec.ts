import { SwitchBoardAppPage } from './app.po';

describe('switch-board-app App', () => {
  let page: SwitchBoardAppPage;

  beforeEach(() => {
    page = new SwitchBoardAppPage();
  });

  it('should display welcome message', () => {
    page.navigateTo();
    expect(page.getParagraphText()).toEqual('Welcome to app!');
  });
});
